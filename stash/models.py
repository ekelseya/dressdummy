from django.db import models
from users.models import User
from patterns.models import PatternType
from fabric.models import Fabric


class PatternStash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(PatternType, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "stash %s %s" % (self.user, self.pattern)


class FabricStash(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "stash %s %s" % (self.user, self.fabric)
