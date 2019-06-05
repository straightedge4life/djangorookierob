# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

from blog.models import comments
from .models import users

# Create your views here.
def commentIndex(request):
    comment_list = comments.objects.order_by('-add_time') 
    asset_data = {
        'comments':comment_list
    }
    return HttpResponse(loader.get_template('comments/index.html').render(asset_data , request))
    
def commentsDetail(request , id):
    q = comments.objects.get(id = id)
    str = 'did you looking for this content:%s'
    return HttpResponse( str % q.content)
        

def latestComment(request):
    res = comments.objects.order_by('-add_time')[:5]
    output = '|'.join([str(v.add_time) for v in res ])
    return HttpResponse(output)