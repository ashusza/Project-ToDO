from django.db import models
from django.utils import timezone

# Create your models here.
class Detail(models.Model):
    task_priority=models.CharField(max_length=200)
    task_code=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.task_priority
    class Meta:
        db_table ='Detail'
        ordering =['-task_priority',]

class Info(models.Model):
    task_name=models.CharField(max_length=100)
    task_create_at=models.DateField(auto_now_add=True)
    priority=models.ForeignKey(Detail,on_delete=models.CASCADE,null=True)
    task_deadline=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.task_name
    
    class Meta:
        db_table='Info'
        ordering=['-task_name',]
    
    