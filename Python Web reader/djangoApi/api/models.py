from django.db import models

# Create your models here.

class Read(models.Model):
    url = models.TextField(blank=False)
    html = models.TextField()
    errorno = models.TextField()
    errormessage = models.TextField()
    
def __str__(self):
        return '%s %s' % (self.url, self.html)