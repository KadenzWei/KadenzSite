"""KadenzSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sheetupload.views import home,pianoSheets,Tutorial,record,aboutMe,manage,sheetUpload,login
#from travel.views import index,user,travelList,edit,pic,manage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^sheetupload/$', sheetupload),
    #############SHEETUPLOAD#############
    url(r'^KadenzPianoSheet/home/$', home),
    url(r'^KadenzPianoSheet/pianoSheets/$', pianoSheets),
    url(r'^KadenzPianoSheet/tutorial/$', Tutorial),
    url(r'^KadenzPianoSheet/record/$', record),
    url(r'^KadenzPianoSheet/aboutMe/$', aboutMe),
    url(r'^KadenzPianoSheet/manage/$', manage),
    url(r'^KadenzPianoSheet/login/$', login),
    url(r'^KadenzPianoSheet/manage/sheetUpload$', sheetUpload),
    #############TRAVEL#############
    # url(r'^travel/index/$', index),
    # url(r'^travel/user/$', user),
    # url(r'^travel/list/$', travelList),
    # url(r'^travel/edit/$', edit),
    # url(r'^travel/pic_upload/$', pic),
    # url(r'^travel/manage/$', manage),
    #url(regex, view)
]