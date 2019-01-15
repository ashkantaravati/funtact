# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from contactbook.serializers import (UserSerializer, GroupSerializer,
                                     ContactBookSerializer, ContactSerializer,
                                     ContactDetailSerializer)
from contactbook.models import Contact, ContactBook, ContactDetail


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ContactBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact books to be viewed or edited.
    """
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact details to be viewed or edited.
    """
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
