from datetime import date
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    create_at = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.title
