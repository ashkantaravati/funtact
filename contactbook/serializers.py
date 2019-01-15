from django.contrib.auth.models import User, Group
from contactbook.models import Contact, ContactBook, ContactDetail
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ContactBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactBook
        fields = (
            'url',
            'label',
            'date_created',
            'user'
        )


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'url',
            'first_name',
            'last_name',
            'note',
            'organization',
            'title',
            'photo',
            'contact_book'
        )


class ContactDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactDetail
        fields = (
            'url',
            'detail_type',
            'value',
            'contact',
        )
