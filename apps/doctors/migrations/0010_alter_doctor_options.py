# Generated by Django 5.0.4 on 2024-04-28 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_alter_doctor_image_for_doctor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'doctor', 'verbose_name_plural': 'doctors'},
        ),
    ]
