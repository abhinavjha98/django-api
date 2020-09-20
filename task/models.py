from django.db import models

# Create your models here.


class activity(models.Model):
  
  start_time = models.CharField(primary_key=True,max_length=200)
  end_time = models.CharField(max_length=200)


class members(models.Model):
  real_name = models.CharField(max_length=200)
  tz = models.CharField(max_length=200)   
  activity_periods = models.ManyToManyField(activity,default=1)
  
  def __str__(self):
    return self.real_name    

   