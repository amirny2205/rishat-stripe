from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'