from djongo import models

# Create your models here.
class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_message = models.TextField()
    updated_date = models.DateTimeField('Last Updated', auto_now=True)