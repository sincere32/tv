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
from django.urls import path
from tv.views import Control, ServersList, ServersAdd, ServersEdit, ServersDelete

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Control.as_view()),
    path('servers/', ServersList.as_view()),
    path('servers/new/', ServersAdd.as_view()),
    path('servers/<int:pk>/', ServersEdit.as_view()),
    path('servers/<int:pk>/delete/', ServersDelete.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
