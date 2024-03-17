from django.db import models


# Create your models here.
class BorrowList(models.Model):
    employee_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
