from rest_framework.serializers import ModelSerializer

from apps.models import BlogPost


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
