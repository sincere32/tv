from django.db import models

SOURCE_TYPES = [
    ('Generic', 'Generic'),
    ('YouTube', 'YouTube')
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
    logo = models.ImageField(upload_to="logos", null=True)
    server = models.ForeignKey(Server, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
