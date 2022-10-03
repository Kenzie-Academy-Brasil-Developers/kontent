from email.policy import default
from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=50)
    module = models.TextField(max_length=None)
    students = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f'<{self.id} {self.title} - {self.module}>'
