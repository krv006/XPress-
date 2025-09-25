from django.db.models import Model, CharField, ImageField, IntegerField


class Footer(Model):
    phone_number = CharField(max_length=200, help_text='Footer uchun telefon raqam kiriting: (929) 566-5040')
    location = CharField(max_length=500)
    gmail_link = CharField(max_length=200, help_text='Gmail link')
    instagram_link = CharField(max_length=200, help_text='Instagram link')
    facebook_link = CharField(max_length=200, help_text='Facebook link')
    youtube_link = CharField(max_length=200, help_text='Youtube link')


class FooterSimple(Model):
    cars_transported = IntegerField()
    satisfied = IntegerField()
    carrier_network = IntegerField()
    star_reviews = IntegerField()


class Partners(Model):
    image = ImageField(upload_to='partners/')
