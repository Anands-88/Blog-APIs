from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view # new schema and documentaion
from rest_framework import permissions # documentation
from drf_yasg import openapi # documentation

schema_view = get_schema_view( # new documentation
    openapi.Info(
        title = "Blog API",
        default_version = "v8",
        description = "A sample API for learning DRF",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path('useradmin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/',include('rest_framework.urls')), # New chapter
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new 
    path('api/v1/dj-rest-auth/registration/', # new
            include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui(# new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(# new
        'redoc', cache_timeout=0), name='schema-redoc'),
]
    