# Generated by Django 4.2.11 on 2024-08-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='test',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
