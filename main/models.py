from django.db import models # type: ignore

# Create your models here.
class Content(models.Model):
    content = models.TextField(verbose_name='content')

    def __str__(self):
        return self.content