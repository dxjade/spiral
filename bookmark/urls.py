from django.conf.urls import url 					#from django.urls import path, re_path (장고2 버젼 용) 2버젼 일단 포기...
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
	url(r'^$', BookmarkLV.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]




"""

urlpatterns = [
	path('', BookmarkLV.as_view(), name='index'),
	path('(?P<pk>\d+)/', BookmarkDV.as_view(), name='detail'),
]


from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV
urlpatterns = [
	url(r'^$', BookmarkLV.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]


from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('index/', views.index, name="index"),
]
"""