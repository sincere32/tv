from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from tv.views import Live


urlpatterns = [
    path('', Live.as_view()),
    path('login', LoginView.as_view(template_name='tv/control/login/login.html')),
    path('login/', LoginView.as_view(template_name='tv/control/login/login.html')),
    path('logout', LogoutView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('admin/', admin.site.urls),
    path('control', include('tv.urls')),
    path('control/', include('tv.urls')),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
