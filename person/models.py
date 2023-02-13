from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.



def is_mail_esprit(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError(
            f"Your email -{value}- must be @esprit.tn")
    return value


def is_cin_length(value):
    if len(value) != 8: 
        raise ValidationError("Your CIN must have 8 characters.")
    return value

class Person(AbstractUser):
    cin = models.CharField(primary_key=True , max_length=8 , validators=[is_cin_length])
    username= models.CharField("Username", max_length=50,unique=True)
    email = models.EmailField("Email", unique=True , validators=[is_mail_esprit])
    USERNAME_FIELD = 'username'

    
    
    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name_plural = "personne"



    

    