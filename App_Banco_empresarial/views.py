from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as login_Django
from django.contrib.auth.decorators import login_required
from random import randint
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
minha_variavel2=[60,
59,
58,
57,
56,
55,
54,
53,
52,
51,
50,

49,
48,
47,
46,
45,
44,
43,
42,
41,
40,

39,
38,
37,
36,
35,
34,
33,
32,
31,
30,

29,
28,
27,
26,
25,
24,
23,
22,
21,
20,

19,
18,
17,
16,
15,
14,
13,
12,
11,
10,

9,
8,
7,
6,
5,
4,
3,
2,
1,
0]

minha_variavel2 = 4563
a=True
import mysql.connector
t=False
teste2=False
conexao= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Celso',
    database='conta_banco_dados'
)

cursor=conexao.cursor(dictionary=True)

minha_variavel = "valor inicial"

@csrf_exempt
def atualizar_variavel(request):
     global minha_variavel
     if request.method == "POST":
        data = json.loads(request.body)
        nova = data.get("nova_variavel", "padrão")
        
        minha_variavel =nova
        print(minha_variavel)
     return render(request,"esqueceu.html")
     
        

def Serviço(request):
     return render(request,"serviço.html")

def Codigo(request):
     minha_variavel=2345
     print(minha_variavel)
     return render(request,"codigo.html",{"nova": minha_variavel})

def Iframe(request):
     return render(request,"Formulario.html")
def Esqueceu(request):
     return render(request,"esqueceu.html")

def Formulario(request):
     return render(request,"Formulario.html")
def Contata(request):
     return render(request,"contata.html")

def Sobre(request):
     return render(request,"sobre.html")

def cadastro(request):

    return render(request,"index.html")

def Home(request):

    return render(request,"index.html")

def Resul_cadastro_cliente(request):
     Nconta2='AO'
     cria_senha2=''


     nome=request.POST.get('nome')
     BI=request.POST.get('bi')
     data_nasc = request.POST.get('data_nasc')
     email=request.POST.get('email')
     telef1=request.POST.get('telef1')
     telef2=request.POST.get('telef2')
     descric=request.POST.get('descric')
     for cont3 in range(0,5):
            cria_senha=str(randint(1,9))
            cria_senha2+=cria_senha

     sexo=request.POST.get('sexo')
     dific=request.POST.get('dificiencia')
     Nconta2=Nconta2+str(randint(0,9))+str(randint(0,9))

     for cont in range(0,3):
             Nconta2+='-'
             for cont2 in range (0,4):
                 
                Nconta2=Nconta2+str(randint(0,9))


     comando=f'INSERT INTO trabalhador(nome,Email,BI,Data_nasc,senha,sexo,Telef1,Telef2,descricao,num_Conta,Dificiencia) VALUES("{nome}","{email}","{BI}","{data_nasc}","{cria_senha2}","{sexo}","{telef1}","{telef2}","{descric}","{Nconta2}","{dific}")'

     cursor.execute(comando)
     

     #res=cursor.fetchall()
     conexao.commit()
     comando=f'select *from trabalhador where nome="{nome}" '
     cursor.execute(comando)
     res2=cursor.fetchall()
     print(res2)
     dados=res2[0]
     return render(request,"Res_cadastro_cliente.html",{'nome':dados['nome'],'dific':dados['Dificiencia'],'Nconta2':dados['num_Conta'],'senha':cria_senha2,'e_mail':email,'numero1':telef1,'numero2':telef2,'data_nasc':data_nasc,'BI':BI})


def Resul_cadastro_empresa(request):
     Nconta2='AO'
     cria_senha2=''


     nome=request.POST.get('nome')
     nome_propet=request.POST.get('nome_propet')
     nif=request.POST.get('nif')
     BI=request.POST.get('bi')
     data_nasc = request.POST.get('data_nasc')
     print(data_nasc)
     email=request.POST.get('email')
     telef1=request.POST.get('telef1')
     telef2=request.POST.get('telef2')
     descric=request.POST.get('descric')
     for cont3 in range(0,5):
            cria_senha=str(randint(1,9))
            cria_senha2+=cria_senha

     sexo=request.POST.get('sexo')

     Nconta2=Nconta2+str(randint(0,9))+str(randint(0,9))

     for cont in range(0,3):
             Nconta2+='-'
             for cont2 in range (0,4):
                 
                Nconta2=Nconta2+str(randint(0,9))


     comando=f'INSERT INTO empresa(nome,nome_propetario,NIF,Email,Telef1,Telef2,descricao,num_Conta) VALUES("{nome}","{nome_propet}","{nif}","{email}","{telef1}","{telef2}","{descric}","{Nconta2}")'
     comando2=f'INSERT INTO propetario(nome_propetario,nome_empresa,BI,Data_nasc,senha,sexo) VALUES("{nome_propet}","{nome}","{BI}","{data_nasc}","{cria_senha2}","{sexo}")'
     
     cursor.execute(comando)
     cursor.execute(comando2)

     #res=cursor.fetchall()
     conexao.commit()
     comando=f'select *from empresa where nome="{nome}" '
     cursor.execute(comando)
     res=cursor.fetchall()
     print(res)
     dados=res[0]
     return render(request,"Res_cadastro_emp.html",{'nome':dados['nome'],'nome_propet':dados['nome_propetario'],'Nconta2':dados['num_Conta'],'senha':cria_senha2,'nif':nif,'e_mail':email,'numero1':telef1,'numero2':telef2})


def login(request):
     a=True
     return render(request,"login.html")

def resultado_login(request):
     res=''
     teste1=False
 
     if request.method == 'GET':
          return render(request,"login.html")
     else:
          nome=request.POST.get('nif')
          senha=request.POST.get('senha')
          comando1=f'select *from propetario where nome_propetario="{nome}" and senha="{senha}"'
          comando2=f'select *from trabalhador where nome="{nome}" and senha="{senha}"'
          comando3=f'select *from empresa where nome_propetario="{nome}"'
          cursor.execute(comando1)
          res=cursor.fetchall()

          cursor.execute(comando2)
          res2=cursor.fetchall()     

          cursor.execute(comando3)
          res3=cursor.fetchall() 

     
          if len(res)!=0:
               
               print(res3)
               return render(request, "Logado_Empresa.html",{'a':a,'Nome':nome,'Nconta2':res3[0]['num_Conta']})
          elif len(res2)!=0:
               return render(request, "Logado_Cliete.html",{'a':a,'Nome':nome,'Nconta2':res3[0]['num_Conta']})
          else:
               messages.warning(request, "Nome ou senha incorreta!")
               teste1=True
               return render(request,'index.html')
               
def publicacao(request):
     a=False
     return render(request,'publicacao.html')
def tranferencia(request):
     return render(request,'tranferencia.html')
def recebido(request):
     return render(request,'recebido.html')
def publicacao(request):
     return render(request,'publicacao.html')
def funcionarios(request):
     return render(request,'funcionarios.html')
def editar(request):
     return render(request,'editar.html')
def tarefas(request):
     return render(request,'tarefas.html')
def chates(request):
     return render(request,'chates.html')
def teste_saldo(request):
     return render(request,'teste_saldo.html')
def dados(request):
     return render(request,'dados.html')



     





