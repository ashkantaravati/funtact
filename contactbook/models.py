' models '
from django.db import models
from django.contrib.auth.models import User

class ContactBook(models.Model):
    'contact book model'
    label = models.CharField(max_length=30)
    date_created = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        pass

class Contact(models.Model):
    'contact model'
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    bio = models.TextField(max_length=240)
    organization = models.CharField(max_length=40)
    title = models.CharField(max_length=10)
    photo = models.ImageField()
    contact_book = models.ForeignKey(ContactBook, on_delete=models.CASCADE)

    def __str__(self):
        pass

class ContactDetail(models.Model):
    'contact detail model'
    detail_type = models.CharField()
    value = models.CharField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    # tel,fax,mobile,pager,Email,postal code,Bio
    def __str__(self):
        pass
        