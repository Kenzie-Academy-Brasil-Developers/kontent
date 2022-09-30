from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=50)
    module = models.CharField(null=False)
    students = models.IntegerField(null=False)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return super().__repr__()
