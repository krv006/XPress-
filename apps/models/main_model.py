from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, BooleanField
from django_ckeditor_5.fields import CKEditor5Field


class MainPage(Model):
    title = CharField(max_length=500)
    name = CharField(max_length=500)
    description = CKEditor5Field()
    content_us = CharField(max_length=100, help_text='Misol uchun: (929) 566-5040')


class ProfessionalTeam(Model):
    name = CharField(max_length=500)
    phone_number = CharField(max_length=100, help_text='Misol uchun: (123) 456-7891')
    by_checking = BooleanField(default=False)

    def clean(self):
        if not self.by_checking:
            raise ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")

    def save(self, *args, **kwargs):
        self.clean()  # clean() ni chaqiramiz
        super().save(*args, **kwargs)


# todo serializer uchun
"""
class ProfessionalTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_Team
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('by_checking') is False:
            raise serializers.ValidationError("Tasdiqlanmagan: submit qilish mumkin emas!")
        return attrs
"""
