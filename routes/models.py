from django.db import models
from django.contrib import admin

# Create your models here. 一個 class 就是一個 table

# 分類(table)
class Category(models.Model):
    Name = models.CharField(max_length = 10, verbose_name='熱門程度') #欄位
    
    # song = models.ManyToManyField('Song', verbose_name='歌曲')
    class Meta: #資料表顯示時的名字
        verbose_name, verbose_name_plural = '類別', '類別'
    def __str__(self): #指到這個 table 時顯示資料的方式
        return self.Name

@admin.register(Category) #將此 model 註冊進 admin 裡
class CategoryAdmin(admin.ModelAdmin): #admin 的管理方式
    list_display = [field.name for field in Category._meta.fields]
    # 管理後台介面顯示的欄位
    search_fields = ('Name',) #去後台可搜尋資料的欄位
    ordering = ('Name',) #搜尋後排序方式

# 歌手資訊(table)
class Artist (models.Model): #歌手
    artist_name = models.TextField(verbose_name='歌手名稱')
    picture = models.ImageField(verbose_name='歌手照片')
    introduce = models.TextField(verbose_name='歌手介紹')
    class Meta: #資料表顯示時的名字
        verbose_name, verbose_name_plural = '歌手資訊', '歌手資訊'
    def __str__(self): #指到這個 table 時顯示資料的方式
        return self.artist

@admin.register(Artist) #將此 model 註冊進 admin 裡
class ArtistAdmin(admin.ModelAdmin): #admin 的管理方式
    list_display = [field.name for field in Artist._meta.fields]
    # 管理後台介面顯示的欄位
    search_fields = ('artist_name',) #去後台可搜尋資料的欄位
    ordering = ('artist_name',) #搜尋後排序方式

# 歌曲資訊(table)
class SongInfo (models.Model):
    # ForeignKey 多筆資料指向一筆資料
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='分類') #分類(table)
    song_name = models.CharField(max_length = 50, verbose_name='歌曲名稱')
    album_name = models.CharField(max_length = 50, verbose_name='專輯名稱')
    artwork = models.ImageField(verbose_name='專輯封面')
    artist = models.ManyToManyField(Artist, verbose_name='歌手')
    year = models.IntegerField(verbose_name='年份')
    style = models.ForeignKey('Style', on_delete=models.CASCADE, verbose_name='曲風') #曲風(table)
    lycris = models.TextField(verbose_name='歌詞')  
    story = models.TextField(verbose_name='故事')
    mv = models.URLField(max_length = 200, verbose_name='MV')
    class Meta: #資料表顯示時的名字
        verbose_name, verbose_name_plural = '歌曲資訊', '歌曲資訊'
    def artist_name(self):
        try:
            return self.artist.artist_name
        except :
            return "invaild"
        

@admin.register(SongInfo) #將此 model 註冊進 admin 裡
class SongInfoAdmin(admin.ModelAdmin): #admin 的管理方式
    # list_display = [field.name for field in SongInfo._meta.fields]
    list_display = ['id','category','song_name','artist_name','style','year']
    # 管理後台介面顯示的欄位
    search_fields = ('category','song_name','artist_name','style','year') #搜尋這些欄位的資料
    ordering = ('song_name',) #排序方式


# 曲風(table)
class Style (models.Model): #曲風
    Name = models.CharField(max_length = 10, verbose_name='曲風名稱') #欄位
    Description = models.TextField(verbose_name='曲風介紹')
    class Meta: #資料表顯示時的名字
        verbose_name, verbose_name_plural = '曲風名稱', '曲風名稱'
    def __str__(self): #指到這個 table 時顯示資料的方式
        return self.Name

@admin.register(Style) #將此 model 註冊進 admin 裡
class StyleAdmin(admin.ModelAdmin): #admin 的管理方式
    list_display = [field.name for field in Style._meta.fields]
    #list_display = ['Name']
    # 管理後台介面顯示的欄位 排序方式等
    search_fields = ('Name',) #當只有一個欄位變數時 set 用的括弧 裡面要有逗號
    ordering = ('Name',) #排序方式
    def __str__(self): #指到這個 table 時顯示資料的方式
        return self.Name + self.Description
