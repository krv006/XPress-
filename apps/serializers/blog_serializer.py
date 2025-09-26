from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost


class BlogModelSerializer(ModelSerializer):
    image_url = SerializerMethodField()
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'short_description', 'published_at', 'views',)
        read_only_fields = ('views',)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y')


class BlogDetailModelSerializer(ModelSerializer):
    image_url = SerializerMethodField()
    published_date = SerializerMethodField()

    class Meta:
        model = BlogPost
        exclude = ('main_image', 'short_description',)
        read_only_fields = ('views',)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None

    def get_published_date(self, obj):
        return obj.published_at.strftime('%B %d %Y')
