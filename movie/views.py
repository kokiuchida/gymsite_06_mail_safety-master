from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Movie

#ログイン必須のページにする
from django.contrib.auth.mixins import LoginRequiredMixin



#DjangoのViewを継承する。クラスベースのビューを作る
#書き方については教科書のP35を参照

#LoginRequiredMixinを追加する。これで未ログインのユーザーはmovieのページにアクセスできない
class MovieView(LoginRequiredMixin,View):

    #GET文(URL指定でアクセスされたときの処理)
    def get(self,request,*args,**kwargs):
        
        if "id" in request.GET:
            #個別の動画ページレンダリングしてレスポンスを返す処理

            data    = Movie.objects.filter(id=request.GET["id"])
            context = { "data": data } 

            print(request.GET["id"])
            return render(request,"movie/content.html",context)

        else:

            print("GET文が送信されました")

            #models.pyのMovieで定義したフィールドに基づき、DBへアクセス
            #movieテーブルに格納されているデータを全て抜き取る
            data    = Movie.objects.all()

            #DBから手に入れたデータをテンプレート変数として渡すため、contextに辞書型として代入
            context = { "data" : data }

            #HTMLの集合体からウェブページを作るため、レンダリング処理をする
            #      レンダリングする(HTTPリクエスト、レンダリング対象のテンプレート、レンダリング対象に与える変数)
            return render(request,"movie/index.html",context)


#urls.pyから呼び出せるように、変数indexの中に処理を格納
index   = MovieView.as_view()

