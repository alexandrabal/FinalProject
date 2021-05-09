"""final_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from .views import homepage_view
from .views import contact_view
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view),
    path('contact/', contact_view),
    path('users/', include('users.urls')),
    path('products/', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# this is the route that specify when this url is accessed- where to go to find the file for example
#     contact view which is gonna be a render of either an html, a redirect.
# the url pattern must be present here even though in users we're bringing it here because django's way of reading
# starts with this directory of urls.py
