from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all_posts.html")

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")
