from django.db import models
from django.db.models import CASCADE


# Create your models here.
class department(models.Model):
    departmentname = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.departmentname)


class course(models.Model):
    deptid = models.ForeignKey(department, on_delete=CASCADE)
    coursename = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.coursename)


