# Generated by Django 2.2 on 2020-10-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
