from django.db import models

# Create your models here.
# import cloudinary
          
# cloudinary.config( 
#   cloud_name = "dwefecwja", 
#   api_key = "918526861367316", 
#   api_secret = "HQIxPKZZUdVz0IaFM71c3dhP9bw" 
# )

class WaitlistEmail(models.Model):
    email = models.CharField(max_length=130, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Waitlist Emails"

    def __str__(self):
        return self.email