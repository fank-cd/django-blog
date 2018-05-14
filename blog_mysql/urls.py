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
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from blog_mysql import views
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader import urls


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'ckeditor', include(urls)),
    url(r'^login/',views.login,name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^comment/',include('comment.urls')),
    url(r'^likes/',include('likes.urls')),
    url(r'^login_for_modal/',views.login_for_modal,name='login_for_medal'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^user_info/', views.user_info, name='user_info'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
