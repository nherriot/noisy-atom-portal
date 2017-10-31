from urllib.parse import quote_plus

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment

from .forms import PostForm
from .models import Post


def create_post(request):
	template_name = 'create.html'

	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False) 
		instance.user = request.user
		instance.save()
		messages.success(request, 'The page successfully created')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request, 'The page not created')

	context = {
		'form': form,
	}
	return render(request, template_name, context)

#retrieve
def detail_post(request, slug=None):
	template_name = 'details.html'

	instance = get_object_or_404(Post, slug=slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	initail_data = {
		'content_type': instance.get_content_type,
		'object_id': instance.id,
	}
	
	comment_form = CommentForm(request.POST or None, initial=initail_data)
	if comment_form.is_valid():
		c_type = comment_form.cleaned_data.get('content_type')
		content_type = ContentType.objects.get(model=c_type)
		obj_id = comment_form.cleaned_data.get('object_id')
		content_data =comment_form.cleaned_data.get('content')
		parent_obj = None

		try:
			parent_id = int(request.POST.get('parent_id'))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
									user = request.user,
									content_type = content_type,
									object_id = obj_id,
									content = content_data,
									parent = parent_obj
								)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = instance.comments

	context = {
		'title': instance.title,
		'instance': instance,
		'share_string': share_string,
		'comments': comments,
		'comment_form': comment_form,
	}

	return render(request, template_name, context)


def list_post(request):
	template_name = 'list.html'

	today = timezone.now().date()
	queryset_list = Post.objects.active()

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all().order_by('-created')

	query = request.GET.get('q')
	
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query) | 
				Q(user__last_name__icontains=query) 
			).distinct()
	
	paginator = Paginator(queryset_list, 2)

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	post_title = Post.objects.all().order_by('-title')

	context = {
			'object_list': queryset,
			'today': today,
		}

	return render(request, template_name, context)

# update
def update_post(request, slug=None):
	template_name = 'update.html'

	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)

	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False) 
		instance.save()
		messages.success(request, 'The page successfully updated')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request, 'Something went wrong with update!')

	context = {
		'title': instance.title,
		'instance': instance.content,
		'slug': instance.slug,
		'image': instance.image,
		'form': form,
	}

	return render(request, template_name, context)

def delete_post(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, 'The post has been deleted')
	return redirect('blogs:list')