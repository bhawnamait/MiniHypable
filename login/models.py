from __future__ import unicode_literals

from time import time

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Articles(models.Model):
    title = models.TextField(max_length=30)
    body = models.TextField('body')
    pub_date = models.DateTimeField('data_published', null=True)
    like = models.IntegerField(default=0, null=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name, null=True)
    user_article = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.id


'''
class Comment(models.Model):
    article = models.ForeignKey(Articles)
    text = models.TextField()
'''
