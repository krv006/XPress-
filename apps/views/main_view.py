from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import MainPage, ProfessionalTeam
from apps.serializers.main_serializer import MainPageModelSerializer, ProfessionalTeamModelSerializer

@extend_schema(tags=["main"])
class MainPageListCreate(ListCreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageModelSerializer
    permission_classes = (AllowAny,)

@extend_schema(tags=["main"])
class ProfessionalTeamListCreate(ListCreateAPIView):
    queryset = ProfessionalTeam.objects.all()
    serializer_class = ProfessionalTeamModelSerializer
    permission_classes = (AllowAny,)
