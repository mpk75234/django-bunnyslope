from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date
