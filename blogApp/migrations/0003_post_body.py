# Generated by Django 3.1.2 on 2020-10-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20201030_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='content'),
            preserve_default=False,
        ),
    ]
