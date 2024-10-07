from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [ 
    path('', views.posts_list, name ='list'), 
    path('post-new', views.posts_new, name ='post-new'), 
    path('<slug:slug>', views.posts_page, name ='page'), 
]
