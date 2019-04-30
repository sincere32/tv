from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    api_port = models.CharField(max_length=5)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Stream(models.Model):
    name = models.CharField(max_length=128)
    source = models.CharField(max_length=2048)
    server = models.ForeignKey(Server, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
