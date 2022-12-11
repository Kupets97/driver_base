from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from raiting.models import Raiting
from comment.models import Comment
from .forms import PersonForm


def index(request):
    form = PersonForm()
    return render(request, 'index.html', {'form': form})


def license(request):
    
    if request.method != 'POST':
        return render(request, 'license.html', {'raiting': ''}, {'comment': ''})

    form = PersonForm(request.POST)

    if not form.is_valid():
        return render(request, 'license.html', {'raiting': 'Веденные данные некорректны'})

    try:
        raiting = Raiting.objects.get(persons__license=form.cleaned_data['license'])
        comments = Comment.objects.filter(person__license=form.cleaned_data['license'])
        return render(request, 'license.html',  {'raiting': raiting.name, 'comments': comments})
    except ObjectDoesNotExist:
        return render(request, 'license.html', {'raiting': 'Такого водителя нет в базе'})

