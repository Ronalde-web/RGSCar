from django.shortcuts import render
from django.http import HttpResponse
from . models import Cliente, Carro

def clientes(request):
    if request.method == "GET":
     return render(request, 'clientes.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('Placas')
        anos = request.POST.getlist('Ano')

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf

            )
    
        #cliente.save()
    
    x = list(zip(carros, placas, anos))

    print(x)
   