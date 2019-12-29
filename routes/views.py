from django.shortcuts import render
from .models import SongInfo


# Create your views here.
#templates裡會用到的檔案 皆在這呼叫
def home(request) :
    return render(request, 'home.html')
def play(request, id) :
    item = SongInfo.objects.get(id=id)
    lyrics = item.lycris.replace('\n', '<br>')
    # SongInfo.objects = SongInfo 下的資料，唯一值使用 get() 取得
    return render(request, 'play.html',{ 'song': item, 'lyrics' : lyrics})
def songlist(request) :
    items = SongInfo.objects.all() # get()中的等號左邊依照 models 下的欄位名稱，等號右邊自己取
    for i in range (len(items)):
        items[i].story = items[i].story.replace('\n', '<br>')
        items[i].artist.all()
    return render(request, 'songlist.html',{ 'songs': items})
def artistpage(request) :
    return render(request, 'artistpage.html')
