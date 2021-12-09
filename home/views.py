from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from home.models import *
from posts.models import *
from .utils import SearchPosts, PaginatePosts

# Create your views here.
def index(request):
    setting= Blog_profile.objects.get()
    category=Category.objects.filter()
    frontpage=Post.objects.filter(frontpage=True)[:1]
    slide1=Post.objects.filter(slide1=True)[:4]
    slide2=Post.objects.filter(slide2=True)[:1]
    slide3=Post.objects.filter(slide3=True)[:1]
    trending=Post.objects.filter(trending_songs=True)[:5] 
    allpost= Post.objects.order_by('-created_at').filter().exclude(category='2')[:6]
    allpost2= Post.objects.order_by('-created_at').filter()[:3]
    sports= Post.objects.order_by('-created_at').filter(category='5')[:6]
    fashion= Post.objects.order_by('-created_at').filter(category='4')[:6]
    politics= Post.objects.order_by('-created_at').filter(category='3')[:6]
    trends= Post.objects.order_by('-created_at').filter(category='6')[:6]
    business= Post.objects.order_by('-created_at').filter(category='7')[:6]
    tech= Post.objects.order_by('-created_at').filter(category='8')[:6]


    context= {
        'setting': setting,
        'category':category,
        'frontpage':frontpage,
        'slide1': slide1,
        'slide2': slide2,
        'slide3': slide3,
        'trending': trending,
        'allpost':allpost,
        'sports':sports,
        'fashion': fashion,
        'politics': politics,
        'allpost2': allpost2,
        'trends': trends,
        'business':business,
        'tech': tech,
    }
    return render (request, 'index.html',context)




def postdetails(request,id,slug):

    

    form= CommentForm(request.POST or None)
    category=Category.objects.all()
    posts= Post.objects.get(pk=id)
    related_post= posts.tags.similar_objects()[:4]
    posted_by=posts.posted_by.get()
    images = Images.objects.filter(post_id=id)
    
    if request.method =='POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            body= request.POST.get('body')
            name= request.POST.get('name')
            comment=Comment.objects.create(post=posts, body=body, name=name)
            comment.save()
        else:
         form= CommentForm()
    

    context={
        'category':category,
        'posts': posts,
        'posted_by': posted_by,
        'images': images,
        'form': form,
        'related_post':related_post,
        # 'commentes':commentes,
    }
    return render(request, 'post-details.html', context)

def about(request):
    category=Category.objects.all()

    context={
        'category':category,
    } 
    return render(request, 'about.html', context)

def search(request):
    posts,search_query=SearchPosts(request)
    category=Category.objects.all()
    custom_range, posts = PaginatePosts(request, posts, 16)

    context={
        'category':category,
        'posts':posts,
        'search_query': search_query,
        'custom_range': custom_range,
    } 
    return render(request, 'search.html', context)

def catposti(request,id,slug):
    category=Category.objects.filter()
    postsss=Post.objects.filter(category_id=id)[:1]
    posts=Post.objects.order_by('-created_at').filter(category_id=id)
    custom_range, posts = PaginatePosts(request, posts, 16)

    
    context={
        'category':category,
        'postsss': postsss,
        'posts':posts,
        'custom_range': custom_range,
    }
    return render(request, 'category.html', context)

def promotion(request):
    setting= Blog_profile.objects.get()
    form = ContactForm
    category=Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message has been sent! Our Service Team will reach out to you soon")
            return redirect('/promotion')

    context={
        'setting': setting,
        'form': form,
        'category':category,
    }
    return render(request, 'promote.html', context)

def privacy(request):
    setting= Blog_profile.objects.get()
    category=Category.objects.all()

    context={
        'setting': setting,
        'category':category,
    }
    return render(request, 'privacy.html', context)