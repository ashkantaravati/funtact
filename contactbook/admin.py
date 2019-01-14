from django.contrib import admin
from contactbook.models import Contact,ContactBook,ContactDetail

# Register your models here.
admin.site.register(ContactBook)
admin.site.register(Contact)
admin.site.register(ContactDetail)
