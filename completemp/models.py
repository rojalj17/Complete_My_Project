from django.db import models


# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class Internal_Guide(models.Model):
    IG=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    ig_name = models.CharField(max_length=200)
    ig_email = models.CharField(max_length=200)
    ig_phone=models.BigIntegerField(default=1)

class Batch(models.Model):
    batch=models.CharField(max_length=200)


class External_Guide(models.Model):
    EG=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    eg_name=models.CharField(max_length=200)
    eg_posts=models.CharField(max_length=200)
    eg_company_name=models.CharField(max_length=50)
    eg_place=models.CharField(max_length=50)
    eg_post_office=models.CharField(max_length=50)
    eg_pin=models.CharField(max_length=50)
    eg_email=models.CharField(max_length=50)
    eg_phone=models.BigIntegerField(default=1)

class Project_schedule(models.Model):
    BATCH=models.ForeignKey(Batch,on_delete=models.CASCADE,default=1)
    # batch_id=models.ForeignKey(batch,default=1,on_delete=models.CASCADE)
    note=models.CharField(max_length=100)
    date=models.CharField(max_length=100,default=1)
    time=models.CharField(max_length=15)

class Chat(models.Model):
    EXTERNAL=models.ForeignKey(External_Guide,on_delete=models.CASCADE,default=1)
    INTERNAL=models.ForeignKey(Internal_Guide,on_delete=models.CASCADE,default=1)
    message=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    send_type=models.CharField(max_length=100)


class Student(models.Model):
    std_name = models.CharField(max_length=200)
    # std_dob = models.CharField(max_length=200)
    # std_gender = models.CharField(max_length=15)
    std_regno = models.CharField(max_length=200)
    # std_group_id = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    std_batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=1)
    # std_course = models.CharField(max_length=50)
    std_email = models.CharField(max_length=50)
    std_phone = models.BigIntegerField(default=1)
    type_mem_lead=models.CharField(max_length=200,default=1)


class Group(models.Model):
    GRP_BATCHID=models.ForeignKey(Batch,on_delete=models.CASCADE,default=1)
    grp_number=models.CharField(max_length=200)
    GRP_IG=models.ForeignKey(Internal_Guide,default=1,on_delete=models.CASCADE)
    GRP_EG=models.ForeignKey(External_Guide,default=1,on_delete=models.CASCADE)
    grp_leader=models.ForeignKey(Student, on_delete=models.CASCADE)
    grp_email=models.CharField(max_length=50)
    grp_topic_name=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)


class Attendance(models.Model):
    # BATCH = models.ForeignKey(Batch, on_delete=models.CASCADE, default=1)
    STD_ID=models.ForeignKey(Student,on_delete=models.CASCADE,default=1)
    GRP_ID=models.ForeignKey(Group,on_delete=models.CASCADE,default=1)
    file=models.CharField(max_length=100)
    date_upload=models.CharField(max_length=100)



class Group_member(models.Model):
    GRP_ID=models.ForeignKey(Group,on_delete=models.CASCADE,default=1)
    LEADER_STUD_ID=models.ForeignKey(Student,on_delete=models.CASCADE,default=1)

class Progress(models.Model):
    GRP = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    progress_file = models.CharField(max_length=100)
    date_upload = models.DateField(max_length=100)
    remark=models.CharField(max_length=500)

class Circular(models.Model):
    GROUP = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    Circular_date=models.CharField(max_length=100)
    Date=models.CharField(max_length=100)
    Time=models.CharField(max_length=100)
    note=models.CharField(max_length=100)

class Scores(models.Model):
    GRP=models.ForeignKey(Group,on_delete=models.CASCADE, default=1)
    Punctuality=models.CharField(max_length=100)
    Relevance=models.CharField(max_length=100)
    Presentation_1=models.CharField(max_length=100)
    Presentation_2=models.CharField(max_length=100)
    Presentation_3=models.CharField(max_length=100)
    Demo_report=models.CharField(max_length=100)
    Institution_copy=models.CharField(max_length=100)
    Viva=models.CharField(max_length=100)
    Total=models.CharField(max_length=100)



