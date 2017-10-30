from django import forms
from core.models import NovoAluno

#Formulários para django

#Arrumar o CursoForms para cadastro de novos cursos, ou mudar nome para cadastro de novos alunos...

#Ver o que está acontecendo com o {% csrf_token %} dentro dos Formulários....

"""class CursoForms(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"
"""


class ContatoForm(forms.Form):

    primeironome = forms.CharField()
    ultimonome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.IntegerField()
    assunto = forms.CharField()
    mensagem = forms.CharField()

    def envia_email(self):
        print(
            "Mensagem do usuário: "+self.cleaned_data["primeironome"]
        )