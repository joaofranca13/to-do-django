from django.db import models


class AddTask(models.Model):
    task = models.CharField(max_length=200)
    complete = models.BooleanField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
