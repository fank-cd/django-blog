"""blog_mysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from blog_mysql import views
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader import urls
urlpatterns = [
    url(r'^$',views.home,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls')),
    url(r'ckeditor',include(urls)),

]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)