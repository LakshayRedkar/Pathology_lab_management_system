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
