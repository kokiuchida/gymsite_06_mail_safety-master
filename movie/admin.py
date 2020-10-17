from django.contrib import admin

# Register your models here.



#教科書P139のリスト13.2に倣って記述。models.pyで定義した内容に基づいて管理ページで編集できるようにする。
from .models import Movie
admin.site.register(Movie)
