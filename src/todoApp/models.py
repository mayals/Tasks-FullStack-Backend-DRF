from django.db import models

# Create your models here.
class Task(models.Model):
    t_name    = models.CharField(max_length=30,blank=False, null=True)
    t_desc    = models.TextField(blank=True, null=True)
    t_created = models.DateTimeField(auto_now_add=True, auto_now=False,blank=False, null=True)
    t_updated = models.DateTimeField(auto_now_add=False, auto_now=True,blank=False, null=True)

    def __str__(self):
        return f'{self.t_name}-{self.t_created}'
    
    class Meta:
        ordering = ('t_name',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        unique_together = ['t_name','t_created']