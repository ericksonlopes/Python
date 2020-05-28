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
from .views import hello, articles, procura_nome, procura_nome_pessoa
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clientes_app

urlpatterns = [
    path('hello/', hello),
    path('articles/<int:anos>', articles),
    path('procura/<str:name>', procura_nome),
    path('procura_pessoa/<str:name>', procura_nome_pessoa),
    path('admin/', admin.site.urls),
    path('person/', include(clientes_app))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
