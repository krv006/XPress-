from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Footer
from apps.models.main_model import MainPage, ProfessionalTeam


@admin.register(MainPage)
class MainPageModelAdmin(ModelAdmin):
    pass


@admin.register(ProfessionalTeam)
class ProfessionalTeamModelAdmin(ModelAdmin):
    pass


@admin.register(Footer)
class FooterModelAdmin(ModelAdmin):
    pass
