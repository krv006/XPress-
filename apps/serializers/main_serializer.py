from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import MainPage,  ProfessionalTeam


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'


class ProfessionalTeamModelSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalTeam
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('by_checking') is False:
            raise ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")
        return attrs
