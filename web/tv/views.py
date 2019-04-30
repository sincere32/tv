from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Server


class Live(TemplateView):
    template_name = 'tv/player.html'


class Control(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tv/control/base.html")

    def post(self, request, *args, **kwargs):
        return render(request, "tv/control/base.html")


class ServersList(View):
    def get(self, request, *args, **kwargs):
        servers = Server.objects.all()
        context = {
            "servers": servers,
        }
        return render(request, "tv/control/servers/index.html", context=context)


class ServersAdd(View):

    def get(self, request, *args, **kwargs):
        from .forms import ServerForm
        form = ServerForm
        context = {
            "form": form,
        }
        return render(request, "tv/control/servers/add.html", context=context)

    def post(self, request, *args, **kwargs):
        from .forms import ServerForm
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "message": "Server "+form.data['name']+" added",
            }
            return render(request, "tv/control/servers/index.html", context=context)
