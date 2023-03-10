from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wsgiref.util import FileWrapper
import io
import json


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

            words.append(word)
            descriptions.append(description)

            id += 1
            word_id = 'word' + str(id)
            description_id = 'description' + str(id)

        data = {'__words__': words, '__descriptions__': descriptions}
        for i in range(len(words)):
            data[words[i]] = descriptions[i]

        return HttpResponseRedirect(f'/crossword/result/data={data}')
    return render(request, './crossword/crossword_creation_form.html')


def get_result_page(request, data):
    data = data[5:].replace("'", '"')
    data = json.loads(data)
    f = io.StringIO()
    f.write(str(data))

    print(f.getvalue())
    response = HttpResponse(f.getvalue(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=file.txt'
    return response
