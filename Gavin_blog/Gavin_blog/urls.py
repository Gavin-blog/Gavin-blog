"""Gavin_blog URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path,include
from Gavin import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$",views.home),
    # 主页
    path("home/",views.home),
    # 文章详情
    re_path(r"^article/(?P<nid>[0-9]*)",views.article),
    # 登录页面
    path("login/",views.login),
    # 注销处理
    path("logout/",views.logout),
    # 管理页面
    path("create_article/",views.create_article),
    # 随笔
    path("new_article/",views.new_article),
    # 删除处理
    path("delete/",views.delete),
    # 分类页面
    re_path("classify_article/(?P<classify>.*)",views.classify_article),
    # 提交评论处理
    path("create_comment/",views.create_comment),
    # 联系方式页面
    path("contact/",views.contact),
    # 添加文章时上传的图片
    path("upload/",views.upload),
    # 添加新分类
    path("new_classify/",views.new_classify)

]
