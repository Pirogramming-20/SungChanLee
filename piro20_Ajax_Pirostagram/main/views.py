from django.shortcuts import render, redirect
from .models import Post, PostLike, Comment
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)
    
import json
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def create_comment(request):  
    req = json.loads(request.body)
    post_id = req['id']
    comment_content = req['comment_content']
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.create(content=comment_content, user=request.user, post=post)
    return JsonResponse({'post_id': post_id, 'comment': comment_content, 'user': comment.user.name, 'comment_id': comment.pk})

@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)          
    comment.delete()
    return JsonResponse({'comment_id': comment_id})
        
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)

    like_objects = PostLike.objects.filter(post=post, user=request.user)
    if like_objects.exists():
        like_objects.delete()
        result = 'like removed'
    else:
        PostLike.objects.create(post=post, user=request.user)
        result = 'like added'

    return JsonResponse({"id": post_id, "result": result})