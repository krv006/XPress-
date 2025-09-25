from django.urls import path

from apps.views.footer_view import FooterListCreate
from apps.views.main_view import MainPageListCreate, ProfessionalTeamListCreate

urlpatterns = [
    path('main-page/', MainPageListCreate.as_view(), name='main_page'),
    path('proffessional-team/', ProfessionalTeamListCreate.as_view(), name='professional_team'),
    path('footer/', FooterListCreate.as_view(), name='footer'),
]
