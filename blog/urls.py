from django.conf.urls import url	# (장고2 버젼 용 from django.urls import path, re_path, url)
from blog.views import *

# app_name='blog'

urlpatterns = [
	url(r'^$', PostLV.as_view(), name='index'),										#3
	url(r'^post/$', PostLV.as_view(), name='post_list'),							#4
	url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),			#5
	url(r'^archive/$', PostAV.as_view(), name='post_archive'),						#6
	url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),		#7
	url(r'^(?P<year>\d{4})/(?P<month>d{2})/$', PostMAV.as_view(), name='post_month_archive'),					#8 영문일경우 정규식 <month>[a-z]{3}
	url(r'^(?P<year>\d{4})/(?P<month>d{2})/(?P<day>\d{1,2})/$', PostMAV.as_view(), name='post_month_archive'),	#9
	url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),					#10
]


"""
	path('', PostLV.as_view(), name='index'),										#3
	path('post/', PostLV.as_view(), name='post_list'),								#4
	path('post/(?P<slug>[-\w]+)', PostDV.as_view(), name='post_detail'),			#5
	path('archive/', PostAV.as_view(), name='post_archive'),						#6
	path('(?P<year>\d{4})/', PostYAV.as_view(), name='post_year_archive'),			#7
	path('(?P<year>\d{4})/(?P<month>d{2})/', PostMAV.as_view(), name='post_month_archive'),					#8 영문일경우 정규식 <month>[a-z]{3}
	path('(?P<year>\d{4})/(?P<month>d{2})/(?P<day>\d{1,2})/', PostMAV.as_view(), name='post_month_archive'),#9
	path('today/', PostTLV.as_view(), name='post_today_archive'),					#10


	이석훈꺼
	from django.conf import settings
	from django.conf.urls import include, url
	from django.conf.urls.static import static
	from django.contrib import admin
	from django.http import HttpResponse
	     
	def hello(request):
		return HttpResponse('''
		<h1>Hello, <a href="http://facebook.com/askdjango/" target="_blank"> AskDjango </a></h1>
		''')

"""
	#url(r'^$', BookmarkLV.as_view(), name='index'),
	#url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
	