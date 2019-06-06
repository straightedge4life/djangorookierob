from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render , get_object_or_404
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