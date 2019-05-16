from django.forms import ModelForm, FileInput
from .models import Server, Channel


class ServerForm (ModelForm):
    class Meta:
        model = Server
        fields = '__all__'


class ChannelForm (ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'
        widgets = {
            'logo': FileInput()
        }
