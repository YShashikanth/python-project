from django.db import models
from django.utils.timezone import now
class UniqueTodo(models.Model):
    task_name = models.CharField(max_length=100)
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=now)
    completed = models.BooleanField(default=False) 
    def _str_(self):
        return self.task_name