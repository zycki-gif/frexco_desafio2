from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from text_generator import generate
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import Cadastro
from .models import Usuario

from .resources import UsersResource


@csrf_exempt
def index(request):
    usuario = Usuario()
    users_qtd = len(Usuario.objects.all())
    if request.method == 'POST':
        form = Cadastro(request.POST)

        if form.is_valid():
            usuario.email = request.POST.get('email')
            usuario.nascimento = request.POST.get('nascimento')

            senha = request.POST.get('senha')

            if not senha:
                senha = generate(length_maximal=20)

            usuario.senha = senha
            usuario.save()

            return HttpResponseRedirect('/api/')
    else:
        form = Cadastro()

    return render(request, 'index.html', {'form': form, 'users': users_qtd})


def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        users_resource = UsersResource()
        dataset = users_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(
                dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(
                dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response
