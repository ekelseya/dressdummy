from django.db import models
from fabric.models import FabricType
from upload_images.models import UploadImage


class PatternCompany(models.Model):
    company = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return "%s" % self.company


class PatternCollection(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(PatternCompany, on_delete=models.CASCADE)
    url = models.URLField(blank=True)

    def __str__(self):
        return "%s" % self.name


class PatternDesigner(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    designs_for = models.ManyToManyField(PatternCompany, blank=True)
    pattern_collections = models.ManyToManyField(PatternCollection, blank=True)

    def __str__(self):
        return "%s" % self.name


class PatternType(models.Model):
    pattern_type = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.pattern_type


class Pattern(models.Model):
    pattern_name = models.CharField(max_length=100)
    pattern_company = models.ForeignKey(PatternCompany, on_delete=models.CASCADE)
    pattern_collection = models.ForeignKey(PatternCollection, blank=True, on_delete=models.CASCADE)
    pattern_designer = models.ForeignKey(PatternDesigner, blank=True, on_delete=models.CASCADE)
    images = models.ManyToManyField(UploadImage, blank=True)
    size = models.CharField(max_length=50)
    url = models.URLField(blank=True)

    def __str__(self):
        return "%s" % self.pattern_name


class PatternView(models.Model):
    pattern_name = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    pattern_type = models.ForeignKey(PatternType, on_delete=models.CASCADE)
    view = models.CharField(max_length=100, default='none')
    fabric_recommendation = models.ManyToManyField(FabricType)
    notions = models.TextField()

    def __str__(self):
        return "%s" % self.view
