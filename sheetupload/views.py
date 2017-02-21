 # -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage
# Create your views here.
#home,pianoSheets,Tutorial,record,aboutMe

def title(content):
    return "Kadenz | "+content

def home(request):
    webTitle = title("Piano Sheet")
    return render_to_response('sheetupload/home.html',locals())

def pianoSheets(request):
    webTitle = title("鋼琴作品")
    return render_to_response('sheetupload/pianoSheets.html',locals())

def Tutorial(request):
    webTitle = title("教學紀錄")
    return render_to_response('sheetupload/tutorial.html',locals())

def record(request):
    webTitle = title("音樂足跡")
    return render_to_response('sheetupload/record.html',locals())

def aboutMe(request):
    webTitle = title("關於我")
    return render_to_response('sheetupload/aboutMe.html',locals())

def manage(request):
    webTitle = title("網站管理")
    return render_to_response('sheetupload/manage.html',locals())

def login(request):
    webTitle = title("登入")
    return render_to_response('sheetupload/login.html',locals())

def sheetUpload(request):
    webTitle = title("樂譜上傳")
    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'sheetupload/sheetUpload.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # return render(request, 'sheetupload/sheetUpload.html')
    return render_to_response('sheetupload/sheetUpload.html',locals())