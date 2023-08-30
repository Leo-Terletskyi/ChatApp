from django.db import models

from django.contrib.auth.models import AbstractUser

from versatileimagefield.fields import VersatileImageField, PPOIField


class User(AbstractUser):
    photo = VersatileImageField(upload_to='images/user_photos/', ppoi_field='photo_ppoi', null=True, blank=True)
    photo_ppoi = PPOIField()
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField('phone number', max_length=14, null=True, blank=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    is_online = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def followers_count(self):
        return self.followers.all().count()
    
    @property
    def following_count(self):
        return self.following.all().count()

    def set_online(self, online=True):
        self.is_online = online
        self.save()
