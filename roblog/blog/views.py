from django.http import HttpResponse , HttpResponseRedirect , HttpRequest
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.utils import timezone

from blog.models import comments
from .models import users

# Create your views here.
def commentIndex(request):
    comment_list = comments.objects.order_by('-add_time') 
    asset_data = {
        'comments':comment_list
    }
    return render(request , 'comments/index.html' , asset_data)
    
def commentsDetail(request , id):
    # try:
    #     q = comments.objects.get(id = id)
    # except comments.DoesNotExist:
    #     raise Http404("id is not exists")


    comment = get_object_or_404(comments , id = id )
    asset_data = {
        'comment' : comment
    }
    
    return render(request , 'comments/detail.html' , asset_data)
        

def latestComment(request):
    res = comments.objects.order_by('-add_time')[:5]
    output = '|'.join([str(v.add_time) for v in res ])
    return HttpResponse(output)

def storeComment(request):
    content = request.POST.get('content')
    comments.objects.create(user_id=0 , content=content  ,add_time=timezone.now())
    #reverse('index' , args=(1,2))
    return HttpResponseRedirect(reverse('index'))

def editComment(request , id):
    comment = get_object_or_404(comments , id=id)
    asset_data = {
        'comment'   : comment
    }
    return render(request , 'comments/edit.html' , asset_data)


def saveComment(request , id):
    content = request.POST.get('content')
    user_id = request.POST.get('user_id')
    comment = get_object_or_404(comments  , id = id)
    comment.content = content
    comment.user_id = user_id
    comment.save()
    return HttpResponseRedirect(reverse('index'))