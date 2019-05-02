from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from .models import Server


class Live(TemplateView):
    template_name = 'tv/player/player.html'


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

class ServersEdit(View):

    def get(self, request, *args, **kwargs):
        from .forms import ServerForm
        server = get_object_or_404(Server,pk=self.kwargs["pk"])
        form = ServerForm(server)
        context = {
            "form": form,
        }
        return render(request, "tv/control/servers/edit.html", context=context)

    def post(self, request, *args, **kwargs):
        from .forms import ServerForm
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "message": "Server "+form.data['name']+" added",
            }
            return render(request, "tv/control/servers/edit.html", context=context)
