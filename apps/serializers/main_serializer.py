from rest_framework.serializers import ModelSerializer

from apps.models import MainPage
from apps.models.main_model import ProfessionalTeam


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'


class ProfessionalTeamModelSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalTeam
        fields = '__all__'
