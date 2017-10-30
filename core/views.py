from django.shortcuts import render
from core.models import *
from core.forms import *

def index(requisicao):

    contexto={
        "faculdade":"FACULDADES PAULISTAS UNIDAS",
        "facul":"FAPALUN",
        "pagina":"HomePage"
    }

    return render(requisicao,"index.html",contexto)


def cadastro(requisicao):
    return render(requisicao,"cadastro.html")



def contato(request):

    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()

    contexto = {
        "form":form
    }

    return render(request,"contato.html",contexto)




def cursos(requisicao):
    return render(requisicao,"cursos.html")



def login(requisicao):
    return render(requisicao,"login.html")



def noticias(requisicao):
    return render(requisicao,"noticias.html")



def novos_alunos(requisicao):
    return render(requisicao,"novos_alunos.html")