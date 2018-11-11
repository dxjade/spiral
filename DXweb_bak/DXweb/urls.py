# < 장고 버전 1.* 용 소스코드 >
from django.contrib import admin
from django.conf.urls import include, url
from DXweb.views import HomeView #181023 add


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),     #181016 add
    url(r'^blog/', include('blog.urls', namespace='blog')),                 #181016 add
    url(r'^$', HomeView.as_view(), name='home')                             #181023 add
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #이진석꺼 먼진 모르지만 주석처리해둠.
"""
# < 장고 버전 1.* 용 소스코드 >
from django.contrib import admin
from django.conf.urls import include, url
        #from bookmark.views import BookmarkLV, BookmarkDV
        #from django.views.generic import ListView, DetailView
        #from bookmark.models import Bookmark #181016 del? 지워야하나? 일단 안지워봄.

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),     #181016 add
    url(r'^blog/', include('blog.urls', namespace='blog')),                 #181016 add
        #Class-based views for bookmark app
        #url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
        #url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),
        #url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
        #url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]





# < 장고 버전 2.* 용 소스코드 >
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),     #181016 add
    path('blog/', include('blog.urls')),             #181016 add
]





"""










"""DXweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""
from django.conf.urls import url
from django.contrib import admin
from bookmark.views import BookmarkLV , BookmarkDV

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
	url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
	
}
"""
"""
from django.contrib import admin
from django.urls import path, include
from bookmark import views
#from . import views

urlpatterns = [
    path('', views.index),               # http://127.0.0.1:8000/ 첫화면 로켓대신, 이걸로 바꿈. from bookmark import views 추가해야하고, bookmark폴더에서 views.py에 코드추가해야함.
    path('admin/', admin.site.urls),
	path('bookmark/', include('bookmark.urls')),
    #path('', admin.site.urls) #루프 주소패턴에 아무것도 없을때 , 예를 들어 (http://127.0.0.1:8000) 치면 어드민 첫 화면으로 가도록 테스트해둠.
    

    #path('', views.home, name='home')  # not defined err
    #path('', views.index)              # not defined err    
]

"""