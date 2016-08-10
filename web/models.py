# -*- cosing: UTF-8 -*-
from django.db import models

class Diary(models.Model):
        memo = models.TextField()
        time = models.DateTimeField(auto_now_add=True)
      
        def __unicode__(self):
                 return self.memo
      
class Month(models.Model):
        date = models.IntegerField(default=0)
    
        def  __unicode__(self):
                 return str(self.date)