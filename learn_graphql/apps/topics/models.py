from django.db import models


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.topic_name
