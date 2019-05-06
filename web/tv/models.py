from django.db import models

SOURCE_TYPES = [
    ('Generic', 'Generic'),
    ('YouTube', 'YouTube')
]

CODEC_CHOICES = [
    ('copy', 'Copy source'),
    ('libx264 -preset ultrafast -crf 23', 'x264 ultrafast CRF23 (Default)'),
    ('libx264 -preset ultrafast -crf 10', 'x264 ultrafast CRF10 (Highest Q)'),
    ('libx264 -preset ultrafast -crf 15', 'x264 ultrafast CRF15 (High Q)'),
    ('libx264 -preset ultrafast -crf 30', 'x264 ultrafast CRF30 (Low Q)'),
    ('libx264 -preset ultrafast -crf 35', 'x264 ultrafast CRF35 (Lowest Q)'),
]


class Server(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    api_port = models.CharField(max_length=5)
    username = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=128)
    source = models.CharField(max_length=2048)
    source_type = models.CharField(
        max_length=128, default='Generic', choices=SOURCE_TYPES)
    codec = models.CharField(
        max_length=128, default='copy', choices=CODEC_CHOICES)
    logo = models.ImageField(upload_to="logos", null=True)
    server = models.ForeignKey(Server, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
