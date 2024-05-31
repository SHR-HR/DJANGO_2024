from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=15, choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced')])
    has_children = models.BooleanField(default=False)

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    school = models.CharField(max_length=100, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    favorite_subject = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    storage_temperature = models.DecimalField(max_digits=4, decimal_places=2)
    shelf_life = models.IntegerField()

class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    business_hours = models.CharField(max_length=50)
    number_of_employees = models.IntegerField()
    average_bill = models.DecimalField(max_digits=6, decimal_places=2)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    ice_creams = models.ManyToManyField(IceCream)
