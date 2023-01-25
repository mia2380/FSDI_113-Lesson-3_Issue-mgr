from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Issue(models.Model):
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='assignee'
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issus_detail', args=[self.id])
