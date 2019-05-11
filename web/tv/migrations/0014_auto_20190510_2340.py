# Generated by Django 2.2.1 on 2019-05-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0013_channel_codec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='codec',
            field=models.CharField(choices=[('copy', 'Copy source'), ('libx264 -preset ultrafast -crf 23', 'x264 ultrafast CRF23 (Default)'), ('libx264 -preset ultrafast -crf 10', 'x264 ultrafast CRF10 (Highest Q)'), ('libx264 -preset ultrafast -crf 15', 'x264 ultrafast CRF15 (High Q)'), ('libx264 -preset ultrafast -crf 30', 'x264 ultrafast CRF30 (Low Q)'), ('libx264 -preset ultrafast -crf 35', 'x264 ultrafast CRF35 (Lowest Q)')], default='copy', max_length=128),
        ),
    ]
