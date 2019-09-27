"""web_create_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin # 後臺管理
from django.urls import path,include # include是用來去查找地方的urls
from django.conf.urls import url #新增
import myapp
# from myapp.views import my_first_web,url_view,index_1st,index_image #新增
# 中央 urls

# 中央的 urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('myapp.urls')),  # 中央urls進行匹配 因正則為空，所以匹配成功
    url(r'^', include('to_do.urls')),  # 9/12註冊to_do app
    url(r'^', include('login.urls')),  # 9/25註冊login
    url(r'^social-auth/', include('social_django.urls', namespace='social')),  # 9/27新增django第三方
]
