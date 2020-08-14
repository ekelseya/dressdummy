from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import date

from patterns.models import PatternView
from stash.models import PatternStash, FabricStash
from upload_images.models import UploadImage

# TODO: info for date input: https://stackoverflow.com/questions/50660580/i-can-not-change-the-date-format-in-django-drf
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(PatternStash, on_delete=models.CASCADE)
    view = models.ForeignKey(PatternView, on_delete=models.CASCADE)
    fabric = models.ManyToManyField(FabricStash)
    notes = models.TextField(blank=True)
    date_started = models.DateField(default=date.today)
    date_finished = models.DateField(blank=True, null=True)
    images = models.ManyToManyField(UploadImage, blank=True)

    def __str__(self):
        return f'{self.user} {self.pattern} project'
