from django.db import models

# Create your models here.

class semester(models.Model):
    course = models.CharField(max_length=50)
    s_id = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)
class Meta:
    db_table="sem"
    ordering=['-id']

class division(models.Model):
    s_id = models.ForeignKey(semester,on_delete=models.CASCADE)
    d_id = models.CharField(max_length=50)
    d_name = models.CharField(max_length=50)
class Meta:
    db_table="div"
    ordering=['-id']

class facultyform(models.Model):
    name=models.CharField(max_length=50)
    faculty_id=models.CharField(max_length=50)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    dep_CHOICES = [
        ('BCA', 'BCA'),
        ('BBA', 'BBA'),
        ('B.com', 'B.com'),
        ('Engineering', 'Engineering'),
        ('Architecture', 'Architecture'),
    ]
    department=models.CharField(max_length=15, choices=dep_CHOICES)
    designation=models.CharField(max_length=50)

class Meta:
    db_table="fac"
    ordering=['-id']

class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Meta:
    db_table="log"
    ordering=['-email']

class feedback(models.Model):
    your_message = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Meta:
    db_table = "feed"
    ordering = ['-email']

class subject(models.Model):
    sub_id = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='text_file/')

class Meta:
    db_table = "subj"
    ordering = ['-id']