 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):

    sku = models.CharField(max_length=13,help_text="Enter Product Stock Keeping Unit")
    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Description")

    def __str__(self):

        return self.title