from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100,default='Default')
    description =models.CharField(max_length=250,default='Default')
    images =models.ImageField(upload_to='portfolio/images/',default='Default')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title
