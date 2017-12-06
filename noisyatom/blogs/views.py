from urllib.parse import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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
        messages.error(request, 'The page is not created')

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

    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,
    }

    return render(request, template_name, context)


def list_post(request):
    template_name = 'list.html'

    today = timezone.now().date()
    queryset_list = Post.objects.active().order_by('-created')

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


    context = {
            'object_list': queryset,
            'today': today,
        }

    return render(request, template_name, context)


def update_post(request, slug=None):
    """
    :param request:
    :param slug:
    :return: HttpResponse, HttpResponseForbidden, Http404, HttpRedirect (302)

    Update a post. This allows a super user or staff user to update a post which is already on the system. It handles HTTP POST/GET
    to do this. The GET method will populate the form and return to the browser. The POST method will store changes into the DB.
    """

    template_name = 'update.html'

    print("=== user ID is: {}".format(request.user))
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden()
    blog_post = get_object_or_404(Post, slug=slug)

    # First check if it's a post. If it is we need to pull values from our form and save them.
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=blog_post)

        if form.is_valid():
            submitted_post = form.save()                    # This returns a post object that is persisted to the database.
            messages.success(request, 'The page successfully updated')
            return HttpResponseRedirect(submitted_post.get_absolute_url())

        else:
            #print("Errors are: {}".format(form.errors))
            messages.success(request, form.errors)
            context = {'form': form}
            return render(request, template_name, context)

    # This must be a http GET message. So populate the form with the blog post from the database and render it in the
    # template.
    form = PostForm(instance=blog_post)
    context = {'form': form}
    return render(request, template_name, context)


def delete_post(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponseForbidden()
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'The post has been deleted')
    return redirect('blogs:list')
