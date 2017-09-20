# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SubmitForm(models.Model):
    name = models.CharField(max_length= 50, null= True, blank= True)
    email = models.EmailField( null= True, blank= True)
    mobile = models.CharField(max_length= 50, null= True, blank= True)
    message = models.TextField(max_length= 3000,  null= True, blank= True)



