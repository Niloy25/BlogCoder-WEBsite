from django.urls import path
from blog import views

urlpatterns = [
    # API to Post a Comment 
    path('postComment', views.postComment, name='postComment'),
    
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]