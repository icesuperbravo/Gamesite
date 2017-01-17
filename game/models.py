from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="Title", unique=True)
    description = models.TextField(default='descr')
    image_url = models.URLField(blank = True)
    quantity = models.IntegerField(default=0)
    def set_title(self, new_title):
        self.title = new_title
        self.save()