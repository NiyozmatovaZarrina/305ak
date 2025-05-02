from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField("name",max_length=20)
    adress=models.CharField("adress",max_length=25)
    phone_number=models.IntegerField("phone_number")
    email=models.EmailField("email")
    website=models.CharField("site",max_length=25)

    class Meta: 
        
        verbose_name="Provider"
        verbose_name_plural="Providers"


    def __str__(self) -> str:
        return self.name




