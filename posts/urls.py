from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import * 

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls