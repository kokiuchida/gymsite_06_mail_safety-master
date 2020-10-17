from django.db import models

# Create your models here.
class Shop(models.Model):
    class Meta:
        #DBのテーブル名を指定する。マイグレーション時にmovieでテーブルが作られる。
        db_table    = "Shop"

    #教科書P47~P48を参照
    #モデルフィールドを定義する。マイグレーションコマンドを実行をすることで、DBに反映できる。
    filename        = models.CharField(verbose_name="画像ファイル名",max_length=200)
    goodsname       = models.CharField(verbose_name="商品の名前",max_length=30)
    price           = models.IntegerField(verbose_name="金額" )
    comment         = models.CharField(verbose_name="商品紹介", max_length=500)


    #管理画面で表示する時の文字列を定義する。
    def __str__(self):
        return self.goodsname

