from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('useradmin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/',include('rest_framework.urls')) # New chapter
]