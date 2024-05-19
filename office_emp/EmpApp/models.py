from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)
    def __str__(self):
         return self.name
         
class Role(models.Model):
        name=models.CharField(max_length=100,null=False)
        def _str_(self):
             return self.name


class Empolly(models. Model):
    first_name=models.CharField(max_length=100,null=False)
    last_Name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bondus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hiredate=models.DateField()
    def _str_(self):
         return "%s %s %s "(self.first_name,self.last_Name,self.phone)
