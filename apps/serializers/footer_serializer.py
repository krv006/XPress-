from rest_framework.serializers import ModelSerializer

from apps.models import Footer,Partners, FooterSimple


class FooterModelSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class PartnerModelSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class FooterSimpleModelSerializer(ModelSerializer):
    class Meta:
        model = FooterSimple
        fields = '__all__'
