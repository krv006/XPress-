from rest_framework.serializers import ModelSerializer

from apps.models import Footer


class FooterModelSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'
