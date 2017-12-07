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
    """

    :param request:
    :return: HttpResponseForbidden, HttpResponse, HttpResponseRedirect

    Creates a new blog post. A super user or staff user creates a new blog post on the system. It handles a HTTP POST/GET to do this.
    For a GET we just populate an empty form into the template. For a POST we validate the submitted form and save in the DB. We store
    the active user in the submitted blog post at the time of creating.
    """

    template_name = 'create.html'

    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden()

    # First check if it's a post. If it is we need to pull values from our form and save them.
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            submitted_blog = form.save(commit=False)
            submitted_blog.user = request.user
            submitted_blog.save()
            messages.success(request, 'The page successfully created')
            return HttpResponseRedirect(submitted_blog.get_absolute_url())
        else:
            messages.error(request, form.errors)

    # This must be a http GET message. So pass an empty Post object into our FORM to be populated by the user.
    form = PostForm()
    context = {'form': form}
    return render(request, template_name, context)


def detail_post(request, slug=None):
    """
    :param request:
    :param slug:
    :return: HttpResponseForbidden, HttpResponse

    Displays the details of a post. This takes the slug to display and renders in the details.html template. It checks to see if the
    post is draft or the publish date is before current date first. If either are true, it only allows staff user or super user to
    view that post. Otherwise it returns a HttpResponseForbidden to the user
    """
    template_name = 'details.html'

    blog_post = get_object_or_404(Post, slug=slug)
    if blog_post.draft or blog_post.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise HttpResponseForbidden

    share_string = quote_plus(blog_post.content)

    context = {
        'title': blog_post.title,
        'instance': blog_post,
        'share_string': share_string,
    }

    return render(request, template_name, context)


def list_post(request):
    """

    :param request:
    :return: HttpResponse

    Displays a list of blog posts that are paginated if more than 5 long. If the user is a super user or staff, all blog posts are
    displayed. If the user is not then only users who have the active flag set to true are displayed.
    """
    template_name = 'list.html'

    today = timezone.now().date()

    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().order_by('-created')
    else:
        queryset_list = Post.objects.active().order_by('-created')

    query = request.GET.get('q')

    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()

    # TODO Make the list of blog posts dynamic. Reading from a value in the settings.py or a parameter in the DB
    paginator = Paginator(queryset_list, 5)
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

    #print("=== user ID is: {}".format(request.user))
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
    """

    :param request:
    :param slug:
    :return: HttpResponseForbidden, Http404, or HttpResponse

    Delete a post. This allows a super user or staff user to delete a post which is already on the system. It handles HTTP POST/GET
    to do this. The GET or POST method will delete the blog post if it exists. Otherwise it will return a Http404. If the user is not
    a super user or staff user it will return a HttpResponseForbidden.
    """

    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden()
    blog_post = get_object_or_404(Post, slug=slug)
    blog_post.delete()
    messages.success(request, 'The post has been deleted')
    return redirect('blogs:list')
