from django.db import models

class MyDataModel(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)


class SchoolDetailModel(models.Model):
    school_name1 = models.CharField(max_length=255)
    school_name2 = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)

# class SectionDetailModel(models.Model):
#     section_type = 
    

