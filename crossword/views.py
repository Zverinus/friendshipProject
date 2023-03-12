import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
import json
import crossword_generator
import empty_crossword
import filled_crossword
import openpyxl
from tempfile import NamedTemporaryFile
from openpyxl.styles import PatternFill, Border, Side, Font

from friendshipProject import settings


def index(request):
    return render(request, './crossword/index.html')


@csrf_exempt
def crossword_creation_form(request):
    if request.method == 'POST':
        words = []
        descriptions = []

        id = 1
        word_id = 'word' + str(id)
        description_id = 'description' + str(id)

        while request.POST.get(word_id):
            word = request.POST.get(word_id)
            description = request.POST.get(description_id)

            if word not in words:
                words.append(word)
                descriptions.append(description)

            id += 1
            word_id = 'word' + str(id)
            description_id = 'description' + str(id)

        data = {'__words__': words, '__descriptions__': descriptions}

        for i in range(len(data["__descriptions__"])):
            if data["__descriptions__"][i] is None:
                data["__descriptions__"][i] = ''
        print(data)
        for i in range(len(words)):
            data[words[i]] = descriptions[i]

        return HttpResponseRedirect(f'/crossword/result/data={data}')
    return render(request, './crossword/crossword_creation_form.html')


@csrf_exempt
def get_result_page(request, data):
    dc = data
    data = data[5:].replace("'", '"')
    data = json.loads(data)

    generator_data = crossword_generator.generate_crossword(data)
    generator_data["descriptions"] = {}
    for word in generator_data["first_letters"].keys():
        generator_data["descriptions"][word] = data[word]
    if request.method == 'POST':
        print(request.POST, 1)
        if 'empty' in request.POST:
            wb = empty_crossword.get_empty_crossword(generator_data)
            with open(wb, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'attachment; filename=empty.xlsx'
                return response
        if 'filled' in request.POST:
            wb = filled_crossword.get_filled_crossword(generator_data)
            with open(wb, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'attachment; filename=filled.xlsx'
                return response

    return render(request, "./crossword/result.html", {'matrix': generator_data["matrix"], 'data': dc})
