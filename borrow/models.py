from django.db import models


# Create your models here.
class BorrowList(models.Model):
    employee_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    section = models.CharField(max_length=100)
    tel = models.IntegerField()
    equipment = models.CharField(max_length=100)
    unit = models.IntegerField
    purpose = models.CharField(max_length=100)
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
