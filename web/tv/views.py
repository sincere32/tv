from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import TemplateView, View
from .models import Server, Channel


class Live(View):
    def get(self, request, *args, **kwargs):
        channels = Channel.objects.all()
        context = {
            "channels": channels,
        }
        return render(request, 'tv/player/player.html', context=context)


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
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/servers/edit.html", context=context)


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
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/servers/edit.html", context=context)


class ServersDelete(View):
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


class ServersTest(View):
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


class ChannelsList(View):
    def get(self, request, *args, **kwargs):
        channels = Channel.objects.all()

        from .modules import docker_control
        for channel in channels:
            client = docker_control.Client(channel)
            status = client.status_channel()
            channel.status = status
        context = {
            "channels": channels,
        }
        return render(request, "tv/control/channels/list.html", context=context)


class ChannelsAdd(View):

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


class ChannelsEdit(View):

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
        form = ChannelForm(request.POST, request.FILES, instance=channel)

        if form.is_valid():
            form.save()
            return redirect(to="../")
        else:
            context = {
                "form": form,
            }
            return render(request, "tv/control/channels/edit.html", context=context)


class ChannelsDelete(View):
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
        channel.delete()
        return redirect(to="/control/channels/")


class ChannelsControl(View):
    def get(self, request, *args, **kwargs):
        channel = get_object_or_404(Channel, pk=self.kwargs["pk"])
        action = self.kwargs["action"]

        from .modules import docker_control
        client = docker_control.Client(channel)

        if client.is_connected:

            if action == "start":
                client.start_channel()
            if action == "stop":
                client.stop_channel()
            if action == "restart":
                client.stop_channel()
                client.start_channel()

        return redirect(to="/control/channels/")
