# Generated by Django 5.0.4 on 2024-04-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='vvedite vashe imya'),
        ),
    ]
