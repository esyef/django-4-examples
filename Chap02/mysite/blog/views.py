from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Post
from django.views.generic import ListView
# from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.


"""
def post_list(request):
    post_list = Post.published.all()

    # Pagination with 3 post per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 
                  'blog/post/list.html', 
                  {'posts': posts})
"""

class PostListView(ListView):
    """
        Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/list.html"



def post_detail(request, year, month,day,post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No post found.')

    # post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


