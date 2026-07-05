from django.db import models
from core.models import BaseModel


class User(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=254, unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.email