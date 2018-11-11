from __future__ import unicode_literals #python2 지원용


from django.db import models # 원래있던것.딱한줄
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible #python2 지원용
class Bookmark(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True) #필드의별칭

	def __str__(self): #객체를 문자열로 표현할때 사용하는 함수
		return self.title

