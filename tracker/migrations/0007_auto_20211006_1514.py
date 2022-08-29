# Generated by Django 3.2.7 on 2021-10-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_coordinate_z'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['created_date']},
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='z',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
