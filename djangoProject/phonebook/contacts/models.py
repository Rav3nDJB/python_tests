from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    contact_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='contact_id')
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=55)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name + ' - ' + self.phone_number
