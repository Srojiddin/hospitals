# Generated by Django 5.0.4 on 2024-04-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_remove_patient_choosing_a_doctor_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='vvedite vashe vozrast'),
        ),
    ]
