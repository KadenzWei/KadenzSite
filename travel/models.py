#encoding=UTF-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TravelList(models.Model):
	name = models.CharField(max_length=100)
	#幾天幾夜
	days = models.DecimalField(max_digits=3,decimal_places=0)
	nights = models.DecimalField(max_digits=3,decimal_places=0)
	#來回日期
	startTime = models.DateTimeField()
	backTime = models.DateTimeField()
	#旅遊地點(簡述)
	place = models.TextField(blank=True)
	#預估支出
	estimatedCost = models.DecimalField(max_digits=5,decimal_places=0)
	#旅遊夥伴
	member = models.TextField(blank=True)
	#備註
	note = models.TextField(blank=True)

	def __str__(self):
		return self.name

class SpotList(models.Model):
	#共同屬性
	time = models.DateTimeField()
	describe = models.TextField(blank=True) #該地方的介紹
	note = models.TextField(blank=True)
	estimatedCost = models.DecimalField(max_digits=5,decimal_places=0,blank=True)
	estimatedTime = models.DecimalField(max_digits=5,decimal_places=0,blank=True) #單位為分鐘
	picture = models.TextField(blank=True) #可存放多張照片
	urllinks = models.TextField(blank=True) #可存放多個連結

	spotType = models.DecimalField(max_digits=1,decimal_places=0)

	#1:單純的景點(名稱,地址)
	spotName = models.CharField(max_length=100, blank=True)
	spotAddress = models.CharField(max_length=100, blank=True)

	#2:交通(交通模式,上車地點,下車地點)
	#交通模式 1:步行,2:腳踏車,3:電動車,4:摩托車,5:火車,6:捷運,7:公車,8:輕軌,9:飛機,10:船)
	transportationType = models.DecimalField(max_digits=1,decimal_places=0, blank=True)
	startPlace = models.CharField(max_length=100, blank=True)
	endPlace = models.CharField(max_length=100, blank=True)

	#3:住宿資訊(旅館名稱,地址,check in,check out time)
	hotelName = models.CharField(max_length=100)
	hotelAddress = models.CharField(max_length=100, blank=True)
	checkinTime = models.DateTimeField(blank=True)
	checkoutTime = models.DateTimeField(blank=True)

	#4:餐廳(名稱,預計食用)
	restaurantName = models.CharField(max_length=100, blank=True)
	restaurantNote = models.CharField(max_length=100, blank=True)

	travelListId = models.ForeignKey(TravelList)

	def __str__(self):
		return self.spotType
