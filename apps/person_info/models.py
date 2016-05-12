# -*- coding: utf-8 -*-*
from django.db import models


class Person(models.Model):
    """Person model"""

    first_name = models.CharField(
        max_length=50,
        blank=False,
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
    )
    date_of_birth = models.DateField(
        blank=False,
    )
    bio = models.TextField(
        blank=True,
        max_length=250,
    )
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(
        max_length=50,
    )
    other_contacts = models.TextField(
        max_length=250,
    )

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)