from django.shortcuts import render

# Create your views here.
#templates裡會用到的檔案 皆在這呼叫
def home(request) :
    return render(request, 'home.html')
def showMusic(request) :
    return render(request, 'showMusic.html')