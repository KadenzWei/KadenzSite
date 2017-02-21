 # -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
	webTitle = '首頁'
	return render_to_response('travel/index.html',locals())

def user(request):
	webTitle = '會員中心'
	return render_to_response('travel/user.html',locals())

def travelList(request):
	webTitle = '旅遊導覽'
	return render_to_response('travel/list.html',locals())

def edit(request):
	webTitle = '編輯'
	return render_to_response('travel/edit.html',locals())

def pic(request):
	webTitle = '圖片上傳'
	return render_to_response('travel/pic.html',locals())

def manage(request):
	webTitle = '系統管理'
	return render_to_response('travel/manage.html',locals())
