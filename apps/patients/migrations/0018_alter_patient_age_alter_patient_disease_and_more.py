# Generated by Django 5.0.4 on 2024-04-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_patient_choosing_a_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='disease',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]