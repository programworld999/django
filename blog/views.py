from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Post
# Create your views here.


def index(request):
    # return HttpResponse("Init Ok")

    data = Post.objects.all()
    return render(request, "blog/index.html", {'data': data})


def post(request):
    if request.GET != "":
        postId = request.GET['id']
        data = Post.objects.filter(id=postId)
        postId = int(postId)

        recomnd = [ Post.objects.filter(id=(str(postId-1))), Post.objects.filter(id=(str(postId-2))), Post.objects.filter(id=(str(postId+1))), Post.objects.filter(id=(str(postId+2))) ]

        context = {
            'data': data,
            'recommended': recomnd
        }

        return render(request, "blog/post.html", context)
    else:
        context = {
            'data': "404"
        }
        return render(request, "blog/error.html", context)

def search(request):
    q = request.GET['q']
    # print(q)
    data = Post.objects.filter(Q(title__icontains=q) | Q(text__icontains=q))
    for res in data:
        print(res.title)
    context = {
        'data': data,
        'search_for': "Search For : " + q,
        "q": q
    }
    return render(request, "blog/index.html", context)
