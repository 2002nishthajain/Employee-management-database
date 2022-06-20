from django.db import models
from django.forms import CharField
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    id = models.CharField(max_length=15,primary_key= 'True')
    Department = models.CharField(max_length=25,unique='True')
    City = models.CharField(max_length=50,default = 'NY Headquaters')
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.Department
    def get_absolute_url(self):
        return reverse('Department_detail', args=[str(self.id)])
    
class Project(models.Model):
    id =models.CharField(max_length=15,primary_key='True')
    Project = models.CharField(max_length=50,unique='True')
    Detail = models.TextField(max_length = 250, default='None')
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.Project
    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
    
class Employees(models.Model) :
    id = models.CharField(max_length=15,verbose_name= 'Emp ID',primary_key= 'True')
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=220)
    Birth_Date = models.DateField()
    Gender_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')]
    Gender = models.CharField(max_length=15,choices=Gender_choices,default='i')
    Hire_Date = models.DateField(default='2022-06-12')
    Position = models.CharField(max_length=220)
    Department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    Project = models.ForeignKey(Project,on_delete=models.SET_NULL, null=True)
    Salary = models.CharField(max_length=15)
    
    class Meta:
        ordering = ['id']   
    def __str__(self):
        return f'{self.First_Name}, {self.Last_Name}'
    def get_absolute_url(self):
        return reverse('Employees_detail', args=[str(self.id)])


#help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'