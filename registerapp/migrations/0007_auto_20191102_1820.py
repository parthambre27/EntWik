# Generated by Django 2.2.6 on 2019-11-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0006_auto_20191102_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='apkfile',
            field=models.FileField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='app',
            name='images',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]
