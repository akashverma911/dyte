from django.db import models

# Create your models here.


class ElasticDemo(models.Model):
    level = models.TextField()
    message = models.TextField()
    resourceId = models.TextField()
    timestamp = models.DateTimeField()
    traceId = models.TextField()
    spanId = models.TextField()
    commit = models.TextField()
    metadata = models.JSONField(null=True, blank=True)
