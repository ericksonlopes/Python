"""meuPrimeiroProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import hello, manda_numero, fname, fname2
from clientes import urls as clientes_urls

urlpatterns = [
    path('busca/<str:name>/', fname),
    path('pesquisa/<str:name>/', fname2),
    path('hello/', hello),
    path('numero/<int:num>/', manda_numero),
    path('admin/', admin.site.urls),
    path('person/', include(clientes_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
