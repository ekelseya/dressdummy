from django.db import models


class FabricType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.type


class RecommendedUses(models.Model):
    uses = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.uses


class DesignElements(models.Model):
    design_elements = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.design_elements


class ColorFamily(models.Model):
    color_family = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.color_family


class FabricBrand(models.Model):
    fabric_brand = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return "%s" % self.fabric_brand


class FabricCollection(models.Model):
    collection = models.CharField(max_length=100)
    brand = models.ManyToManyField(FabricBrand)
    year_released = models.IntegerField(blank=True)

    def __str__(self):
        return "%s" % self.collection


class Designer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    designs_for = models.ManyToManyField(FabricBrand)
    fabric_collections = models.ManyToManyField(FabricCollection, blank=True)

    def __str__(self):
        return "%s" % self.name


class Fabric(models.Model):
    name = models.CharField(max_length=100)
    image = models.ManyToManyField('upload_images.UploadImage', blank=True)
    designer = models.ForeignKey(Designer, blank=True, on_delete=models.CASCADE)
    fabric_collection = models.ForeignKey(FabricCollection, blank=True, on_delete=models.CASCADE)
    fabric_type = models.ForeignKey(FabricType, blank=True, on_delete=models.CASCADE)
    recommended_uses = models.ManyToManyField(RecommendedUses, blank=True)
    design_elements = models.ManyToManyField(DesignElements, blank=True)
    color_family = models.ManyToManyField(ColorFamily)

    def __str__(self):
        return "%s" % self.name
