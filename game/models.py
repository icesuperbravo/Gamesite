from django.db import models
from django.forms import ModelForm

# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    """
    TODO: add developer field when authentication is implemented
    developer = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    """
    title = models.CharField(max_length=255, default="Title", unique=True)
    description = models.TextField(default='descr')
    image_url = models.URLField(blank = True)
    def set_title(self, new_title):
        self.title = new_title
        self.save()

class CreateGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'image_url']


class DeleteGameForm(ModelForm):
    class Meta:
        model = Game
        fields = []

""" TODO: HighsCore model - with fields game, score, and user """