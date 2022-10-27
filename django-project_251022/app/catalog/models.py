from django.db import models
from django.urls import reverse 

# Create your models here.
class Student(models.Model):
    Student_ID = models.AutoField(primary_key = True)
    forename = models.CharField(max_length=100, default='Some string')
    surname = models.CharField(max_length=100, default='some string')
    dob = models.DateField(null=True, blank=True)

    #address = models.ForeignKey('StudentAddress', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.forename} {self.surname}, {self.dob}'
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('student-detail', args=[str(self.id)])
    
class StudentAddress(models.Model):
    address_id = models.AutoField(primary_key = True)
    Student_ID = models.ForeignKey('Student',on_delete=models.SET_NULL, null=True)
    house_number = models.IntegerField(null=True)
    first_line = models.CharField(max_length=200)
    post_code = models.CharField(max_length=100)
    town = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.house_number}, {self.first_line}, {self.post_code, self.town}'

    def get_absolute_url(self):
        """Returns the URL to access a particular student instance."""
        return reverse('address-detail', args=[str(self.id)])
