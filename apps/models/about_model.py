from django.db.models import Model, CharField
from django_ckeditor_5.fields import CKEditor5Field


class About(Model):
    title = CharField()
    description = CKEditor5Field()


class FAQ(Model):
    title = CharField()
    description = CKEditor5Field()
