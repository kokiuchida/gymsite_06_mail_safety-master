"""config URL Configuration

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
from django.contrib import admin

from django.urls import path,include


#書き方は教科書のP27を参照
#URLと処理の関係を入力していく。それがurls.py
#path(URL,実行する処理(さらに参照するurls.py),URL逆引き用の名前指定)
#allauthでのログインを実装させる
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls"),name="home"),
    path('movie/', include("movie.urls"),name="movie"),
    path('staff/', include("staff.urls"),name="staff"),
    path('shop/', include("shop.urls"),name="shop"),
    path('accounts/', include("allauth.urls")),
]
