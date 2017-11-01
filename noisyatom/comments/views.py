from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from .forms import CommentForm
from .models import Comment 


def comment_thread(request, id):
	template_name = 'comment_thread.html'

	## need to make permission
	try:
		obj = Comment.objects.get(id=id)
	except:
		raise Http404

	content_object = obj.content_object
	content_id = obj.content_object.id

	initail_data = {
		'content_type': obj.content_type,
		'object_id': obj.object_id
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

	context = {
		'comment': obj,
		'comment_form':comment_form
	}
	return render(request, template_name, context)


def comment_delete(request, id):
	template_name = 'confirm_delete.html'

	try:
		obj = Comment.objects.get(id=id)
	except:
		raise Http404

	if obj.user != request.user:
		response = HttpResponse('You do not have permisstion to delete this comment')
		response.status_code = 403
		return response 

	if request.method == 'POST':
		parent_obj_url = obj.content_object.get_absolute_url()
		obj.delete()
		messages.success(request, 'The comment has been deleted!')
		return HttpResponseRedirect(parent_obj_url)
	context = {
		'object': obj
	}
	return render(request, template_name, context)
