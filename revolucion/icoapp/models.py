from django.db import models
from usersapp.models import NewUser


# Create your models here.
class Ico(models.Model):
    # id создается автомитически
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField()
    starts = models.CharField(max_length=16)
    ends = models.CharField(max_length=16)
    rating = models.FloatField()
    url = models.URLField()
    # user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
