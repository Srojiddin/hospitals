# Generated by Django 5.0.4 on 2024-04-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_doctor_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
