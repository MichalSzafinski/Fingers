"""ml_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
from accounts.views import (
    login_view,
    logout_view,
    register_view,
    login_error_view,
)
from prediction.views import (
    home_view,
    upload_photo_view,
    UploadView
)


router = routers.DefaultRouter()
router.register('upload', UploadView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('send/', upload_photo_view),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('login_error/', login_error_view),
    path('register/', register_view, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
