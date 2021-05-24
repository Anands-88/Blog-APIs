from django.urls import path
from .views import * 

urlpatterns = [
    path('post/<int:pk>/', PostDetail.as_view()),
    path('post/', PostList.as_view()), 
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('comment/',CommentList.as_view()),
]