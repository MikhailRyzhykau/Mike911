import json

from django.conf import settings
from django.shortcuts import redirect, render

from .forms import InputForm
from .models import InputModel


def index(request):
    templates = 'index.html'
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['fild1']
            data = json.dumps(name_input, ensure_ascii=False)
            InputModel.objects.create(data=data, field='fild')
            settings.LAST_FILDS = 1
            for count in range(2, len(request.POST)):
                query = 'fild' + str(count)
                input_value = request.POST[query]
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data, field=field)
                settings.LAST_FILDS = count
        return redirect('/done/')
    else:
        form = InputForm()
    context = {'form': form}
    return render(request, templates, context)


def done(request):
    templates = 'done.html'
    query = InputModel.objects.all().values('id', 'field', 'data')
    json_list = list(query)
    last_write = json_list[-settings.LAST_FILDS:]
    context = {
        'json_list': json_list,
        'last_write': last_write,
    }
    return render(request, templates, context)


def clear_bd(request):
    query = InputModel.objects.all()
    query.delete()
    return redirect('/')
