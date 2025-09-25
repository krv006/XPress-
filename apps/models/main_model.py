from django.db.models import Model, CharField, BooleanField
from django_ckeditor_5.fields import CKEditor5Field


class MainPage(Model):
    title = CharField(max_length=500)
    name = CharField(max_length=500)
    description = CKEditor5Field()
    content_us = CharField(max_length=100, help_text='Misol uchun: (929) 566-5040')


class ProfessionalTeam(Model):
    name = CharField(max_length=500)
    phone_number = CharField(max_length=100, help_text='Misol uchun: (123) 456-7891')
    by_checking = BooleanField(default=False)
