# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class blogy(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	author = models.ForeignKey(User,null=True)
	date_created = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=250,null=True)
	pic = models.FileField(upload_to = 'pic',null=True)

	def __unicode__(self):
		return self.title


class comment(models.Model):
	post = models.ForeignKey(blogy,blank=True,null=True)
	cmt_user = models.ForeignKey(User,blank=True,null=True)
	user_cmnt = models.CharField(max_length=300,blank=True,null=True)
	date = models.DateTimeField(auto_now=True, blank=True,null=True)

	def __unicode__(self):
		return self.user_cmnt

