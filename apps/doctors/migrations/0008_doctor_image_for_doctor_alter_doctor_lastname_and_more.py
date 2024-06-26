# Generated by Django 5.0.4 on 2024-04-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_alter_doctor_age_alter_doctor_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image_for_doctor',
            field=models.ImageField(default=1, upload_to='blogs/', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=30),
        ),
    ]
