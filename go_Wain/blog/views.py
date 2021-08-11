from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    data = Blogpost.objects.all()
    print(data, "this is data")
    return render(request, 'blog/index.html', {"param": data})


def blogpost(request, id):
    data = Blogpost.objects.get(post_id=id)
    idset = Blogpost.objects.all()
    length = len(idset)
    # print(data, "this is data")
    # print(length, "this is idset")
    return render(request, 'blog/blogpost.html', {"param": data,"idset":idset,"length":length})
