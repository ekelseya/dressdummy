from django.db import models
from django.contrib.auth.models import User
from patterns.models import PatternView
from stash.models import PatternStash, FabricStash


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(PatternStash, on_delete=models.CASCADE)
    view = models.ForeignKey(PatternView, on_delete=models.CASCADE)
    fabric = models.ManyToManyField(FabricStash)
    notes = models.TextField(blank=True)
    # add images

    def __str__(self):
        return "project %s %s" % (self.user, self.pattern)
