from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class AdminProfile(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='admin/')
    intro = HTMLField('intro', blank=True)
    education = HTMLField('education', blank=True)
    experience = HTMLField('experience', blank=True)
    hobbies = HTMLField('hobbies', blank=True)
    contact_me = HTMLField('contact_me', blank=True)
    about = HTMLField('about', blank=True)

    def __str__(self):
        return f'Admin Profile'
