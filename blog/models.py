from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateField()
    
    def __str__(self):
        return self.title
