from django.shortcuts import render

def index(requisicao):

    contexto={
        "faculdade":"FACULDADES PAULISTAS UNIDAS",
        "facul":"FAPALUN",
        "pagina":"HomePage"
    }

    return render(requisicao,"index.html",contexto)