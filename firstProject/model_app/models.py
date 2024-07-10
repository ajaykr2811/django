from django.db import models


class person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.TextField()
    elgible = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    