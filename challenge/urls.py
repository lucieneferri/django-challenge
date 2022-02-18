
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.db import router
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, AuthorViewSet, ArticleViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'sign-up', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', views.obtain_auth_token),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
