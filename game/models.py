from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from django.db.models.signals import post_save
from django.dispatch import receiver

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
    creator = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='created_games')
    def set_title(self, new_title):
        self.title = new_title
        self.save()



""" TODO: HighsCore model - with fields game, score, and user """


#class UserType(Enum):
#    GAMER = 1
#    DEVELOPER = 2

#class UserDetails(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    role = UserType


class Profile(models.Model):
    USERTYPE_PLAYER = 0
    USERTYPE_DEVELOPER = 1
    USERTYPE_CHOICES = (
        (USERTYPE_PLAYER, 'Player'),
        (USERTYPE_DEVELOPER, 'Developer'),
    )
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    usertype = models.IntegerField(choices=USERTYPE_CHOICES, null=True)
    owned_games = models.ManyToManyField(Game)

    def is_developer(self):
        return (self.usertype == 1)




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
