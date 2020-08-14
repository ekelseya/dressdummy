from django.db import models
from django.contrib.auth.models import User
from patterns.models import Pattern
from fabric.models import Fabric


class PatternStash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "stash %s %s" % (self.user, self.pattern)


class FabricStash(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    length = models.CharField(max_length=10, blank=True, null=True)
    notes = models.TextField(blank=True)
    # Add "used" boolean

    def __str__(self):
        return "stash %s %s" % (self.user, self.fabric)
