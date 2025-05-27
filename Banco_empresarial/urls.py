"""
URL configuration for Banco_empresarial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from App_Banco_empresarial import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.cadastro,name='home'),
    path('res/',views.Resul_cadastro_empresa,name='res_cadast'),
    path('Criar Conta/',views.login,name='login'),
    path('Empresa/',views.resultado_login,name='resultado_login'),
    path('Home/',views.Home,name='home'),
    path('cadastro_cliente',views.Resul_cadastro_cliente, name='cadastro_cliente'),
    path('publicacao/',views.publicacao,name='publicacao'),
    path('tranferencia/',views.tranferencia,name='tranferencia'),
    path('recebido/',views.recebido,name='recebido'),
    path('funcionarios/',views.funcionarios,name='funcionarios'),
    path('editar/',views.editar,name='editar'),
    path('tarefas/',views.tarefas,name='tarefas'),
    path('chates/',views.chates,name='chates'),
    path('dados/',views.dados,name='dados'),
    path('teste_saldo/',views.teste_saldo,name='teste_saldo'),
    path('Serviços/',views.Serviço,name='serviço'),
    path('Sobre/',views.Sobre,name='sobre'),
    path('Contata-nos/',views.Contata,name='contata'),
    path('Formulario/',views.Formulario,name='formulario'),
    path('Iframe/',views.Iframe,name='iframe'),
    path('Esqueceu/',views.Esqueceu,name='esqueceu'),
    path('Codigo/',views.Codigo,name='codigo'),
    path('atualizar-variavel/', views.atualizar_variavel, name='atualizar_variavel'),


   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
