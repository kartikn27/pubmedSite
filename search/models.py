from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
    document_id = models.CharField(max_length = 64, default='DEFAULT VALUE')
    title = models.CharField(max_length = 1028)
    summary = models.CharField(max_length = 15000)
    year = models.IntegerField
    pubmed_id = models.IntegerField
    journal = models.CharField(max_length = 512)
    pubmed_central_id = models.IntegerField
