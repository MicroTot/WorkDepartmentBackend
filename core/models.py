from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)

    class Meta:
        ordering = ("-id",)
    def __str__(self):
        return self.name