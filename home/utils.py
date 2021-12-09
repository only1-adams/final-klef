from posts.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def PaginatePosts(request, posts, results):

    page=request.GET.get('page')
    paginator=Paginator(posts,results)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        page=1
        posts=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        posts=paginator.page(page)
    
    leftIndex= (int(page) - 1)
    if leftIndex < 1:
        leftIndex=1

    rightIndex= (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1


    
    custom_range= range(leftIndex,rightIndex)

    return custom_range, posts


def SearchPosts(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query', '')
    
    posts= Post.objects.filter(title1__icontains=search_query)

    return posts, search_query