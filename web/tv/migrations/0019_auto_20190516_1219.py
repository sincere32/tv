# Generated by Django 2.2.1 on 2019-05-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0018_auto_20190516_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='logo',
            field=models.BinaryField(editable=True),
        ),
    ]
