# Generated by Django 3.1.2 on 2020-10-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_auto_20201031_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image_url',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
    ]