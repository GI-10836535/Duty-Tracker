# Generated by Django 4.1 on 2022-09-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0003_rename_percentage_extraworkreport_percentage_done_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigneddutyactivities',
            name='rating',
            field=models.CharField(default='Unrated', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recieveddutyreports',
            name='rating',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
