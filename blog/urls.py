from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post', views.post, name="post"),
    url(r"^search", views.search, name="search"),
    
]
