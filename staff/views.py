from django.shortcuts import render

# Create your views here.

#クラスベースのビューを作るため
from django.views import View
from .models import Staff

#Viewを継承してGET文、POST文の関数を作る
class StaffView(View):

    def get(self, request, *args, **kwargs):

        data    = Staff.objects.all()
        context = { "data" : data }

        return render(request,"staff/index.html",context)

    def post(self, request, *args, **kwargs):

        pass

index   = StaffView.as_view()


