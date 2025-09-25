from rest_framework.serializers import ModelSerializer

from apps.models import Main_Page
from apps.models.main_model import ProfessionalTeam


class MainPageModelSerializer(ModelSerializer):
    class Meta:
        model = Main_Page
        fields = '__all__'


class ProfessionalTeamModelSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalTeam
        fields = '__all__'
