from django.shortcuts import render
from .models import SongInfo


# Create your views here.
#templates裡會用到的檔案 皆在這呼叫
def home(request) :
    return render(request, 'home.html')
def play(request, id) :
    item = SongInfo.objects.get(id=id)
    lyric = item.lycris.replace('\n', '<br>')
    # SongInfo.objects = SongInfo 下的資料，唯一值使用 get() 取得
    return render(request, 'play.html',{ 'song': item, 'lycris' : lyric})
def songlist(request) :
    return render(request, 'songlist.html')
def artistpage(request) :
    return render(request, 'artistpage.html')
