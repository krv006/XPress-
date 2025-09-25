from django.utils.html import strip_tags
from import_export import fields
from import_export.resources import ModelResource

from apps.models import MainPage


class MainPageResource(ModelResource):
    description = fields.Field(
        column_name='description'
    )

    class Meta:
        model = MainPage
        fields = ('id', 'title', 'description')

    def dehydrate_description(self, obj):
        return strip_tags(obj.description)

    def before_import_row(self, row, **kwargs):
        if "description" in row and row["description"]:
            row["description"] = strip_tags(row["description"])
