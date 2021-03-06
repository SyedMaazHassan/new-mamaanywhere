# Generated by Django 4.0.3 on 2022-05-18 22:36

from django.db import migrations, models
import webapp.storages


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0040_zoomlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPrivate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=webapp.storages.PrivateMediaStorage(), upload_to='')),
            ],
        ),
    ]
