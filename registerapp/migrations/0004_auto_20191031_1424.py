# Generated by Django 2.2.6 on 2019-10-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0003_auto_20191030_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='longdesc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='privpolicy',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='promovideo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='shortdesc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
