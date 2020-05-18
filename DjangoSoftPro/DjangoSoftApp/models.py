from django.db import models

from multiselectfield import MultiSelectField


class FeedbackDatabase(models.Model):
    name = models.CharField(max_length=100)
    ratting = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    Feedback = models.CharField(max_length=100)

class ContactDatabase(models.Model):
    Name = models.CharField(max_length=100)
    Mobile_Number = models.BigIntegerField()
    Email = models.EmailField(max_length=100)
    COURSES_CHOICES = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Ui', 'Ui'),
        ('Rest Api', 'Rest Api'),
        ('Flask', 'Flask'),
        ('Mysql', 'Mysql'),
    )
    courses = MultiSelectField(max_length=200, choices=COURSES_CHOICES)
    TRAINERS_CHOICES = (
        ('Narayana', 'Narayana'),
        ('Mahesh', 'Mahesh'),
        ('Mohan Reddy', 'Mohan Reddy'),
        ('Srinivas', 'Srinivas'),
        ('Wilson', 'Wilson')
    )
    trainers = MultiSelectField(max_length=200, choices=TRAINERS_CHOICES)
    LOCATIONS_CHOICES = (
        ('Hyd', 'Hyd'),
        ('Bang', 'Bang'),
        ('Pune', 'Pune'),
        ('Delhi', 'Delhi'),
        ('Chennai', 'Chennai')
    )
    locations = MultiSelectField(max_length=200, choices=LOCATIONS_CHOICES)
    SHIFTS_CHOICES = (
        ('Morning', "Morning"),
        ('After Noon', "After Noon"),
        ('Evening', 'Evening'),
        ('Night', 'Night')
    )
    shifts = MultiSelectField(max_length=100, choices=SHIFTS_CHOICES)
    gender = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)



class VegetableDatabase(models.Model):
    Product_name = models.CharField(max_length=200, blank=True)
    MRP = models.IntegerField(blank=True)
    Price =models.IntegerField(blank=True)
    Save = models.IntegerField(blank=True)
    Big_image = models.ImageField(upload_to='Vegetables/', blank=True)
    First_image = models.ImageField(upload_to='Vegetables/', blank=True)
    Second_image = models.ImageField(upload_to='Vegetables/', blank=True)
    Category_CHOICES = (
        ('Nothing', 'Nothing'),
        ('Popularity', 'Popularity'),
        ('Best Selling', 'Best Selling'),
    )
    Category = MultiSelectField(max_length=200,choices=Category_CHOICES)
    About_product = models.CharField(max_length=500, blank=True)
    Storage = models.CharField(max_length=100, blank=True)
    Benefits = models.CharField(max_length=500, blank=True)
    Weight_policy = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.Product_name

class FruitsDatabase(models.Model):
    Product_name = models.CharField(max_length=200, blank=True)
    MRP = models.IntegerField(blank=True)
    Price =models.IntegerField(blank=True)
    Save = models.IntegerField(blank=True)
    Big_image = models.ImageField(upload_to='Fruits/', blank=True)
    First_image = models.ImageField(upload_to='Fruits/', blank=True)
    Second_image = models.ImageField(upload_to='Fruits/', blank=True)
    Category_CHOICES = (
        ('Nothing', 'Nothing'),
        ('Popularity', 'Popularity'),
        ('Best Selling', 'Best Selling'),
    )
    Category = MultiSelectField(max_length=200,choices=Category_CHOICES)
    About_product = models.CharField(max_length=500, blank=True)
    Storage = models.CharField(max_length=100, blank=True)
    Benefits = models.CharField(max_length=500, blank=True)
    Weight_policy = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.Product_name