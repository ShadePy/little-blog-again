from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogging/post/list.html'

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)  # 3 posts per page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # if page is not an integer - render first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # if page is out of range - render last page
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'posts': posts,
#         'page': page
#     }
#     return render(request, 'blogging/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status='published',
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {
        'post': post
    }
    return render(request, 'blogging/post/detail.html', context)
