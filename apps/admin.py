from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from apps.models import Footer
from apps.models.main_model import MainPage, ProfessionalTeam
from apps.resources import MainPageResource


@admin.register(MainPage)
class MainPageModelAdmin(ImportExportModelAdmin):
    resource_class = MainPageResource


@admin.register(ProfessionalTeam)
class ProfessionalTeamModelAdmin(ModelAdmin):
    pass


@admin.register(Footer)
class FooterModelAdmin(ModelAdmin):
    pass
