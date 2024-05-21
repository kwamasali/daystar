from django.db import models

# Create your models here.
class Type_stay(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name    
    
class Babies(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    
    #Linking baby to have a type_of_stay
    typestay = models.ForeignKey(Type_stay, on_delete=models.CASCADE)

    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
    parent = models.CharField(max_length=50, null=True, blank=True)
    student_number = models.CharField(max_length=40, null=True, blank=True)
    gaurdian = models.CharField(max_length=10, null=True, blank=True)
    baby_id = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payee = models.ForeignKey(Babies, on_delete=models.CASCADE)
    typestay = models.ForeignKey(Type_stay, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    payer = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.payer 
      
class Sitter(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.CharField(max_length=10, null=True, blank=True)
    religion = models.CharField(max_length=10, null=True, blank=True)
    sitter_number = models.CharField(max_length=40, null=True, blank=True)
    level_of_education = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
   
    def __str__(self):
        return self.name

class DollsShop(models.Model):
    item = models.CharField(max_length=70, null=False, blank=False)
    amount = models.IntegerField( null=True, blank=True)
    num_available = models.IntegerField( null=True, blank=True)
    payer = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.item
    
class CheckIn(models.Model):

    date = models.CharField(max_length=70, null=False, blank=False)
    baby = models.ForeignKey(Babies, on_delete=models.CASCADE)
    time_in = models.TimeField(null=False, blank=False)
    time_out = models.TimeField(null=False, blank=False)
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    payment_to_sitter = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return self.date