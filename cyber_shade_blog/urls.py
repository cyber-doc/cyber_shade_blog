"""
URL configuration for cyber_shade_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import urls as blog_urls
from users import urls as users_urls
from core import urls as core_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include(blog_urls)),
    path('', include(users_urls)),
    path('', include(core_urls)),

]
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'),
         name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
