# Generated by Django 2.1.5 on 2019-05-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0009_auto_20190502_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos/'),
        ),
    ]
