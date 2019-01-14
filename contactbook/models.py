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
    note = models.TextField(max_length=240)
    organization = models.CharField(max_length=40)
    title = models.CharField(max_length=10)
    photo = models.ImageField()
    contact_book = models.ForeignKey(ContactBook, on_delete=models.CASCADE)

    def __str__(self):
        pass

class ContactDetail(models.Model):
    'contact detail model'
    # detail type choices:
    WORK = 'WK'
    PHONE = 'PN'
    HOME = 'HM'
    FAX = 'FX'
    EMAIL = 'EM'
    ADDRESS = 'AD'
    POSTAL_CODE = 'PC'
    WEB_ADDRESS = 'WA'
    EVENT = 'EV' #will also need type specification for itself
    MESSENGER_ACCOUNT = 'MA'

    DETAIL_TYPE_CHOICES = (
        (WORK, 'Work Phone Number'),
        (PHONE, 'Cell Phone Number'),
        (HOME, 'Home Phone Number'),
        (FAX, 'Fax Number'),
        (ADDRESS, 'Address'), # Will need more chars than other items
        (POSTAL_CODE, 'Zip/Postal Code'),
        (WEB_ADDRESS, 'Website or Blog'),
        (EVENT, 'Birthday, Anniversary, etc.'),
        (MESSENGER_ACCOUNT, 'WhatsApp, Telegram, Messenger, etc.')
    )
    detail_type = models.CharField(max_length=2, choices=DETAIL_TYPE_CHOICES, default=PHONE)
    value = models.CharField(max_length=200) # will need validation somehow
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    
    def __str__(self):
        pass
        