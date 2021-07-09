from django.db import models

class AHashData(models.Model):
    image = models.ImageField(upload_to='ahash_img')
    ahash = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'lec05'
        db_table = 'ahash_data'