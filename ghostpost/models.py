from django.db import models
from django.utils import timezone


class Post(models.Model):
    b_or_r = models.BooleanField(
        help_text="Checked is Boast, Unchecked is Roast")
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    # Citation: Used to figure out total_vote calculation
    # https://stackoverflow.com/
    # questions/60226890/how-to-add-variable-in-django-model
    @property
    def total_vote(self):
        return self.up_vote - self.down_vote

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-created',)
