# Generated by Django 3.2.7 on 2021-09-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210907_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='no-image.png', null=True, upload_to=''),
        ),
    ]
