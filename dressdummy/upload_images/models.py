from django.db import models


class UploadImage(models.Model):

    image = models.FileField(blank=False, null=False)
