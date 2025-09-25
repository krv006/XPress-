from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Footer
from apps.serializers.footer_serializer import FooterModelSerializer

@extend_schema(tags=["footer"])
class FooterListCreate(ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterModelSerializer
    permission_classes = (AllowAny,)
