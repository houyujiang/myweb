# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth = models.DateField(blank=True ,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)