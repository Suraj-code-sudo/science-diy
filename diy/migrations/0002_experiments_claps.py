# Generated by Django 3.2.15 on 2022-09-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiments',
            name='claps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
