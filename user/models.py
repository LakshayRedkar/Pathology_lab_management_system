from django.db import models

# Create your models here.

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(unique=True, max_length=255)
    patient_email = models.CharField(unique=True, max_length=255)
    patient_password = models.CharField(max_length=255)
    patient_dob = models.DateField(blank=True, null=True)
    patient_gender = models.CharField(max_length=45, blank=True, null=True)
    patient_status = models.IntegerField(blank=True, null=True)
    patient_phone_number = models.CharField(unique=True, max_length=12, blank=True, null=True)
  
    class Meta:
        managed = False
        db_table = 'patients'

class LabTest(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=191)
    test_cost = models.CharField(max_length=191)
    lab_test_image = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'lab_test'

class BookedTest(models.Model):
    book_id = models.AutoField(primary_key=True)
    p_id= models.ForeignKey('Patients', models.DO_NOTHING)
    b_date = models.DateTimeField()
    tests = models.CharField(max_length=25)
    booking_status = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'booked_test'

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    pat_id = models.IntegerField(blank=True, null=True)
    b_date = models.DateTimeField(blank=True, null=True)
    booking_status = models.IntegerField(blank=True, null=True)
    test_name = models.CharField(max_length=45, blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'book'