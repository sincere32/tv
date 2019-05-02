from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
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
        return render(request, "tv/control/servers/list.html", context=context)


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
            return render(request, "tv/control/servers/list.html", context=context)


class ServersEdit(View):

    def get(self, request, *args, **kwargs):
        from .forms import ServerForm
        server = get_object_or_404(Server, pk=self.kwargs["pk"])
        form = ServerForm(instance=server)
        context = {
            "form": form,
        }
        return render(request, "tv/control/servers/edit.html", context=context)

    def post(self, request, *args, **kwargs):
        from .forms import ServerForm
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect("/control/servers/")

class ServersDelete(View):
    def get(self, request, *args, **kwargs):
        from .forms import ServerForm
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        form = ServerForm(request.POST, instance=server)
        context = {
            "server":server,
            "form":form,
        }
        return render(request, "tv/control/servers/delete.html", context=context)

    def post(self, request, *args, **kwargs):
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        server.delete()
        return redirect("/control/servers/")
