from django.shortcuts import render
from .models import SongInfo, Category, Artist, Style

# Create your views here.
#templates裡會用到的檔案 皆在這呼叫

def home(request) : 
    return render(request, 'home.html') # render = 回傳 HttpResponse
def play(request, id) :
    item = SongInfo.objects.get(id=id)
    lyrics = item.lycris.replace('\n', '<br>')
    # SongInfo.objects = SongInfo 下的資料，唯一值使用 get() 取得
    return render(request, 'play.html',{ 'song': item, 'lyrics' : lyrics})
def songlist_category(request, category) :
    items = SongInfo.objects.filter(category=Category.objects.get(Name=category)) # get()中的等號左邊依照 models 下的欄位名稱，等號右邊自己取
    for i in range (len(items)):
        items[i].story = items[i].story.replace('\n', '<br>')
        items[i].artist.all()
    return render(request, 'songlist.html',{ 'songs': items})
def songlist_style(request, style) :
    items = SongInfo.objects.filter(style=Style.objects.get(Name=style)) # get()中的等號左邊依照 models 下的欄位名稱，等號右邊自己取
    for i in range (len(items)):
        items[i].story = items[i].story.replace('\n', '<br>')
        items[i].artist.all()
    return render(request, 'songlist.html',{ 'songs': items})
def artistpage(request, id) :
    artist = Artist.objects.get(id=id)
    items = SongInfo.objects.filter(artist=artist)
    introduce = artist.introduce.replace('\n', '<br>')
    return render(request, 'artistpage.html',{ 'songs': items, 'artist':artist, 'introduce' : introduce})
