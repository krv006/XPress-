from django.db.models import Model, ImageField, CharField, DateTimeField, PositiveIntegerField, SlugField
from django.db.models.indexes import Index
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


def cover_upload_to(instance, filename):
    return f"blog/{instance.slug or slugify(instance.title)}/{filename}"


class BlogPost(Model):
    title = CharField(max_length=160)
    short_description = CKEditor5Field()
    long_description = CKEditor5Field()
    published_at = DateTimeField(default=timezone.now)
    main_image = ImageField(upload_to=cover_upload_to, blank=True, null=True, help_text="Main image")
    back_image = ImageField(upload_to=cover_upload_to, blank=True, null=True, help_text="Detail image")
    url = CharField(max_length=500)
    views = PositiveIntegerField(default=0)
    slug = SlugField(max_length=180, unique=True, blank=True)

    class Meta:
        ordering = ["-published_at"]
        indexes = [
            Index(fields=["-published_at"]),
            Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            base = slugify(self.title)[:170]
            slug = base
            i = 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug

        return super().save(*args, **kwargs)
