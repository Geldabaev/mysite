# Generated by Django 4.2.3 on 2023-07-28 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]