# Generated by Django 3.1.2 on 2020-10-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
    ]