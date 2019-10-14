from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    firstname = models.CharField(_('First Name'), default="John", max_length=20)
    lastname = models.CharField(_('Last Name'), default="Doe", max_length=20)
    tenth = models.FloatField(_('10th Percentage'), default= 0, max_length=100)
    twelveth = models.FloatField(_('12th Percentage'), default= 0, max_length=100)
    engaggr = models.FloatField(_('Engineering Aggregate (Percentile)'), default= 0, max_length='4')

    def __str__(self):
        return f'{self.user.username} Profile'


# messes up registration
#    def save(self):
 #       super(Profile, self).save(*args, **kwargs)
 #       prof = Image.open(self.image.path)
 #       if prof.height>300 or prof.width > 300:
 #           output_size = (300, 300)
 #           prof.thumbnail(output_size)
 #           prof.save(self.image.path)

class Grievances(models.Model):
    g_username = models.CharField(_('Username:'), default="", max_length=30)
    company_name = models.CharField(_('Company Name:'), default="", max_length=30)
    user_query = models.TextField(_('Question:'), default="Q. ", max_length=200,)
    is_answered = models.BooleanField(_('Is Answered?:'), default=False)

    def __str__(self):
        return f'{self.company_name} - {self.user_query}'
