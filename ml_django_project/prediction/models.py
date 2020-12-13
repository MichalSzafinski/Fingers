from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save


User = get_user_model()


class Upload(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    prediction = models.CharField(max_length=500, default='None')
    chance = models.CharField(max_length=500, default='None')

    def get_path(self):
        return self.image.url
