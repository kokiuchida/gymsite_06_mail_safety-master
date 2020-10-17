from django.shortcuts import render

# Create your views here.

#クラスベースのビューを作るため
from django.views import View
from .models import Shop

#Viewを継承してGET文、POST文の関数を作る
class ShopView(View):

    def get(self, request, *args, **kwargs):

        data    = Shop.objects.all()
        context = { "data" : data }

        return render(request,"shop/index.html",context)

    def post(self, request, *args, **kwargs):

        pass

index   = ShopView.as_view()


