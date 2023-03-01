from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, './crossword/index.html')


def crossword_creation_form(request):
    return render(request, './crossword/crossword_creation_form.html')
