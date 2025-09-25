from django.db.models import Model, CharField, DateTimeField, ImageField
from django_ckeditor_5.fields import CKEditor5Field


class BlogPost(Model):
    title = CharField()
    description = CKEditor5Field()
    created = DateTimeField(auto_now_add=True)
    image = ImageField(upload_to='blog_posts/')
    url = CharField()
