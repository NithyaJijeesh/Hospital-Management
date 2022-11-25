from distutils.command.upload import upload
from re import M
from django.db import models
from django.contrib.auth.models import User #,AbstractUser


# Create your models here.
'''class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)'''

class room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=255)
    room_charge = models.IntegerField(null=True)

    def __str__(self):
        return self.room_type

class qualification(models.Model):
    
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.qualification

class department(models.Model):
    
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qualification = models.ForeignKey(qualification,on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact_num = models.IntegerField(max_length=12)
    gender = models.CharField(max_length=10)
    joining_date = models.DateField()
    profile_pic = models.ImageField(null = True,blank = True, upload_to = 'image/doctor')
    fees = models.IntegerField()

    def __str__(self):
        return self.user

class patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(room,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    contact_num = models.IntegerField(max_length=12)
    email = models.EmailField(null=True)
    patient_type = models.IntegerField()
    consulting_date = models.DateField(null=True)
    admission_date = models.DateField(null=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')

    def __str__(self) :
        return self.first_name

class prescription(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    medicine_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255,null=True,blank=True)

class path_test(models.Model):
    test_name = models.CharField(max_length=255)
    charge = models.IntegerField()

class pathology(models.Model):
    patient = models.ForeignKey(patient,on_delete= models.CASCADE)
    path_test = models.ForeignKey(path_test,on_delete=models.CASCADE)
    test_date = models.DateField()
    description = models.CharField(max_length=255,null=True)
    

class inpatient_bill(models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    #room = models.ForeignKey(room,on_delete=models.CASCADE,null=True)
    #doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    #pathology = models.ForeignKey(pathology,on_delete=models.CASCADE,null=True)
    bill_date = models.DateField()
    discharge_date = models.DateField()
    total = models.IntegerField(null=True)

class outpatient_bill(models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    #doctor = models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    #pathology = models.ForeignKey(pathology,on_delete=models.CASCADE,null=True,blank=True)
    bill_date = models.DateField()
    total = models.IntegerField(null=True)

class appointment(models.Model):
    patient=models.ForeignKey(patient,on_delete=models.CASCADE, null=True)
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE, null=True)
    appointment_date=models.DateField(null=True)
    description=models.TextField(max_length=500)
    status=models.IntegerField(default=False,null=True)



    
