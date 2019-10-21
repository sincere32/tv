from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Server, Channel
from .modules import docker_control


class Live(View):
    def get(self, request, *args, **kwargs):
        channels = Channel.objects.all().order_by('name')
        context = {
            "channels": channels,
        }
        return render(request, 'tv/player/player.html', context=context)


class ServersList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        servers = Server.objects.all()
        context = {
            "servers": servers,
        }
        return render(request, "tv/control/servers/list.html", context=context)


class ServersAdd(LoginRequiredMixin, View):

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
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/servers/edit.html", context=context)


class ServersEdit(LoginRequiredMixin, View):

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
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/servers/edit.html", context=context)


class ServersDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        from .forms import ServerForm
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        form = ServerForm(request.POST, instance=server)
        context = {
            "server": server,
            "form": form,
        }
        return render(request, "tv/control/servers/delete.html", context=context)

    def post(self, request, *args, **kwargs):
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        server.delete()
        return redirect(to="/control/servers/")


class ServersTest(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        import docker
        docker_url = "http://"+server.address+":"+server.api_port
        client = docker.DockerClient(base_url=docker_url)
        try:
            info = client.info()
            context = {
                "server": server,
                "info": info,
            }
            return render(request, "tv/control/servers/test.html", context=context)
        except:
            context = {
                "server": server,
                "message": "Failed to establish a new connection to "+docker_url,
            }
            return render(request, "tv/control/servers/test.html", context=context)


class ChannelsList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        channels = Channel.objects.all().order_by('name')
        from .modules import docker_control
        for channel in channels:
            try:
                client = docker_control.Client(channel)
                channel.container = client.get_container()
            except:
                channel.container = "Not found !"
        context = {
            "channels": channels,
        }
        return render(request, "tv/control/channels/list.html", context=context)


class ChannelsAdd(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        from .forms import ChannelForm
        form = ChannelForm
        context = {
            "form": form,
        }
        return render(request, "tv/control/channels/add.html", context=context)

    def post(self, request, *args, **kwargs):
        from .forms import ChannelForm
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            channels = Channel.objects.all()
            context = {
                "channels": channels,
            }
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/channels/edit.html", context=context)


class ChannelsEdit(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        from .forms import ChannelForm
        channel = get_object_or_404(Channel, pk=self.kwargs["pk"])
        form = ChannelForm(instance=channel)
        context = {
            "form": form,
        }
        return render(request, "tv/control/channels/edit.html", context=context)

    def post(self, request, *args, **kwargs):
        from .forms import ChannelForm
        channel = get_object_or_404(Channel, pk=self.kwargs["pk"])
        client = docker_control.Client(channel)

        form = ChannelForm(request.POST, request.FILES, instance=channel)

        if form.is_valid():
            client.rename_channel(name=form.data['name'])
            form.save()
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/channels/edit.html", context=context)


class ChannelsDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        from .forms import ChannelForm
        channel = get_object_or_404(Channel, pk=self.kwargs["pk"])
        form = ChannelForm(request.POST, instance=channel)
        context = {
            "channel": channel,
            "form": form,
        }
        return render(request, "tv/control/channels/delete.html", context=context)

    def post(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=self.kwargs['pk'])
        client = docker_control.Client(channel)
        client.delete_channel()
        channel.delete()
        return redirect(to="/control/channels/")


class ChannelsControl(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=self.kwargs["pk"])
        action = self.kwargs["action"]

        client = docker_control.Client(channel)

        if client.connected:

            if action == "start":
                client.start_channel()
            if action == "stop":
                client.stop_channel()
            if action == "restart":
                client.stop_channel()
                client.start_channel()
            if action == "recreate":
                client.recreate_channel()
            if action == "stats":
                stats = client.get_stats()

        return redirect(to="/control/channels/")
