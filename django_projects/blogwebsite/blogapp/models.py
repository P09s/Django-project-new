from django.db import models

# Create your models here.
class BlogDetail(models.Model):
  blog_id = models.AutoField(primary_key=True)
  blog_title = models.CharField(max_length=50)
  blog_desc = models.CharField(max_length=250)
  blog_date=models.DateField()
  class Meta:
      db_table = "BlogTable" 

class library(models.Model):
  book_id = models.AutoField(primary_key=True)
  book_title = models.CharField(max_length=50)
  book_desc = models.CharField(max_length=250)
  book_date=models.DateField()
  class Meta:
      db_table = "libraryTable" 

     



