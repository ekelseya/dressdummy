from django.db import models


class FabricType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.type}'


class FabricContent(models.Model):
    content = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.content}'


class RecommendedUse(models.Model):
    uses = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.uses}'


class DesignElement(models.Model):
    design_elements = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.design_elements}'


class ColorFamily(models.Model):
    color_family = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.color_family}'


class FabricBrand(models.Model):
    fabric_brand = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return f'{self.fabric_brand}'


class FabricCollection(models.Model):
    collection = models.CharField(max_length=100)
    brand = models.ManyToManyField(FabricBrand)
    year_released = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.collection}'


class Designer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    designs_for = models.ManyToManyField(FabricBrand)
    fabric_collections = models.ManyToManyField(FabricCollection, blank=True)

    def __str__(self):
        return f'{self.name}'


class Fabric(models.Model):
    name = models.CharField(max_length=100)
    image = models.ManyToManyField('upload_images.UploadImage', blank=True, null=True)
    brand = models.ForeignKey(FabricBrand, blank=True, null=True, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, blank=True, null=True, on_delete=models.CASCADE)
    fabric_collection = models.ForeignKey(FabricCollection, blank=True, null=True, on_delete=models.CASCADE)
    fabric_type = models.ForeignKey(FabricType, blank=True, null=True, on_delete=models.CASCADE)
    fabric_content = models.ForeignKey(FabricContent, blank=True, null=True, on_delete=models.CASCADE)
    recommended_uses = models.ManyToManyField(RecommendedUse, blank=True, null=True)
    design_elements = models.ManyToManyField(DesignElement, blank=True, null=True)
    color_family = models.ManyToManyField(ColorFamily, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
