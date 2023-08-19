from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Usuario
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return JsonResponse({"message": "Bem-vindo à API de Usuários!"})

def criar_usuario(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']

        try:
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        except ValueError:
            return HttpResponse("Data de nascimento inválida.")

        novo_usuario = Usuario.objects.create(cpf=cpf, nome=nome, data_nascimento=data_nascimento)
        novo_usuario.save()

        # Renderize a página 'usuario_criado.html' e retorne como resposta
        return render(request, 'usuario_criado.html') 

    return render(request, 'criar_usuario.html')  # Renderizar o formulário novamente


def obter_usuario(request):
    if request.method == 'GET':
        cpf = request.GET.get('cpf')
        
        try:
            usuario = Usuario.objects.filter(cpf=cpf).first()
            
            if usuario:
                return render(request, 'usuario.html', {'usuario': usuario})
            else:
                # Retorne uma resposta HTTP com uma mensagem de erro (ex.: "Usuário não encontrado")
                return HttpResponse("Usuário não encontrado")
        except Usuario.MultipleObjectsReturned:
            # Retorne uma resposta HTTP com uma mensagem de erro (ex.: "Mais de um usuário encontrado")
            return HttpResponse("Mais de um usuário encontrado")        
    return render(request, 'obter_usuario.html')

def usuario_criado(request):
    return render(request, 'usuario_criado.html')