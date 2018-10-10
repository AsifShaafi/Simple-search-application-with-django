"""assignmentProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path

from searchapp import views

urlpatterns = [
    url(r'^api/developers/$', views.DeveloperList.as_view(), name="all_developers"),
    path('api/developers/add', views.DeveloperAdd.as_view(), name="add_developer"),
    path('api/developers/<int:pk>', views.DeveloperDetail.as_view(), name='developer_details'),
    path('admin/', admin.site.urls),
    path('', include('searchapp.urls')),
]

