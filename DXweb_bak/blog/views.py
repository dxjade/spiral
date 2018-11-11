#from django.shortcuts import render #원래있던것인데 책엔 없길레 일단 주석 처리함.181016

# Create your views here.
"""
from django.shortcuts import render # 뭔진모르지만 이석훈꺼 ㅋ
    def post_list(request):
        return render(request, 'blog/post_list.html') #하나의 뷰를 만들고, 템플릿만든다


"""
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'
    month_format = '%m' #한글경우add

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


