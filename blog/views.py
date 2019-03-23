from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Init Ok")
    return render(request, "blog/index.html", {data: "JHGF"})
