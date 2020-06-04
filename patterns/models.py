from django.db import models
from fabric.models import FabricType
from upload_images.models import UploadImage


class PatternCompany(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f'{self.company}'


class PatternCollection(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(PatternCompany, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    year_published = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class PatternDesigner(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    designs_for = models.ManyToManyField(PatternCompany, blank=True)
    pattern_collections = models.ManyToManyField(PatternCollection, blank=True)

    def __str__(self):
        return f'{self.name}'


class PatternType(models.Model):
    pattern_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pattern_type}'


class Pattern(models.Model):
    pattern_name = models.CharField(max_length=100)
    pattern_company = models.ForeignKey(PatternCompany, on_delete=models.CASCADE)
    pattern_collection = models.ForeignKey(PatternCollection, blank=True, null=True, on_delete=models.CASCADE)
    pattern_designer = models.ForeignKey(PatternDesigner, blank=True, null=True, on_delete=models.CASCADE)
    images = models.ManyToManyField(UploadImage, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.pattern_name}'


class PatternView(models.Model):
    pattern_name = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    pattern_type = models.ForeignKey(PatternType, on_delete=models.CASCADE)
    view = models.CharField(max_length=100, default='none')
    description = models.TextField(blank=True)
    fabric_recommendation = models.ManyToManyField(FabricType)
    notions = models.TextField(blank=True)

    def __str__(self):
        return f'{self.view}'


class PatternSize(models.Model):
    pattern_view = models.ForeignKey(PatternView, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.size}'


class PatternFinishedMeasurement(models.Model):
    pattern_size = models.ForeignKey(PatternSize, on_delete=models.CASCADE)
    bust = models.CharField(max_length=10)
    waist = models.CharField(max_length=10)
    hip = models.CharField(max_length=10)

    def __str__(self):
        return f'Bust: {self.bust} Waist: {self.waist} Hip: {self.hip}'
