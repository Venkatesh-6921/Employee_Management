from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()
    Job_role= models.TextField()
    Salary = models.PositiveIntegerField()
    Date_Of_Joining =models.DateField()
    Department=models.TextField()
    

    def __str__(self):
        return self.name