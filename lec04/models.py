from django.db import models


class ImageData(models.Model):
    image = models.ImageField(upload_to='img')
    r = models.FloatField()
    g = models.FloatField()
    b = models.FloatField()
    upload_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'lec04'
        db_table = 'image_data'