# -*- coding: utf-8 -*-
from django.db import models
class Topic(models.Model):
#�û�ѧϰ������
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
#����ģ�͵��ַ�����ʾ
		return self.text

