# Generated by Django 2.2.14 on 2022-11-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dummy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]