from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    object_list = Post.objects.all()
    
    paginator = Paginator(object_list, 1) # 3 posts in each page
    try :
        page = request.GET.get('page')
    except :
        page=1
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/post/list.html',
                        {'page': page,
                        'posts': posts})
    
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
    post.visits = post.visits +1 
    post.save()
        
    return render(request,
        'blog/post/detail.html',
        {'post': post})
def post_share(request, post_id):
    sent = False
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    
    if request.method == 'POST':
    # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Form fields passed validation
            cd = form.cleaned_data
        # ... send email
        post_url = request.build_absolute_uri(
            post.get_absolute_url())
        subject = f"{cd['name']} recommends you read " \
                    f"{post.title}"
        message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'admin@myblog.com',
                    [cd['to']])
        sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
    