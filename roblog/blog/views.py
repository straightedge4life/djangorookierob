# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render
from django.http import Http404

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
    try:
        q = comments.objects.get(id = id)
    except comments.DoesNotExist:
        raise Http404("id is not exists")

    str = 'did you looking for this content:%s'
    return HttpResponse( str % q.content)
        

def latestComment(request):
    res = comments.objects.order_by('-add_time')[:5]
    output = '|'.join([str(v.add_time) for v in res ])
    return HttpResponse(output)