"""site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from filebrowser.sites import site

from project import settings

urlpatterns = [
  url(r'^select2/', include('django_select2.urls')),
  url(r'^admin/filebrowser/', site.urls),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
  url(r'^admin/?', admin.site.urls),
  url(r'^core/?', include('core.urls')),
  url(r'^', include('frontend.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)