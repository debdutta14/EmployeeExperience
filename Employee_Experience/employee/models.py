from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=30, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=20, default="new")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    date_of_joining=models.DateField()
    last_date=models.DateField()