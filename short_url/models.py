from django.contrib.auth.models import User
from django.db import models


class Links(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')
    short_url = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    url = models.CharField(max_length=512)
    description = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.description}: {self.short_url}'
