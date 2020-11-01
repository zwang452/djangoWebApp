# Generated by Django 3.1.2 on 2020-10-31 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_catogory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catogory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogApp.catogory'),
        ),
        migrations.AlterField(
            model_name='catogory',
            name='catogoryName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
