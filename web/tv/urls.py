"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import Control
from .views import ServersList, ServersAdd, ServersEdit, ServersDelete, ServersTest
from .views import ChannelsList, ChannelsAdd, ChannelsEdit, ChannelsDelete,ChannelsControl

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Control.as_view()),
    path('servers/', ServersList.as_view()),
    path('servers/new/', ServersAdd.as_view()),
    path('servers/<int:pk>/', ServersEdit.as_view()),
    path('servers/<int:pk>/delete/', ServersDelete.as_view()),
    path('servers/<int:pk>/test/', ServersTest.as_view()),
    path('channels/', ChannelsList.as_view()),
    path('channels/new/', ChannelsAdd.as_view()),
    path('channels/<int:pk>/', ChannelsEdit.as_view()),
    path('channels/<int:pk>/delete/', ChannelsDelete.as_view()),
    path('channels/<int:pk>/<str:action>/', ChannelsControl.as_view()),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
