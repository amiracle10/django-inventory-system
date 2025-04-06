from django.db import models

# Create your models here.
class Discussion(models.Model):
    title = models.CharField(max_length=100)
    snippet = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title