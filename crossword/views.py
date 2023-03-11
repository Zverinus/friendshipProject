from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
import json
import crossword_generator


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

        print(data)
        for i in range(len(words)):
            data[words[i]] = descriptions[i]

        return HttpResponseRedirect(f'/crossword/result/data={data}')
    return render(request, './crossword/crossword_creation_form.html')


def get_result_page(request, data):
    data = data[5:].replace("'", '"')
    data = json.loads(data)

    generator_data = crossword_generator.generate_crossword(data)

    f = io.StringIO()
    for i in generator_data["matrix"]:
        f.write("".join(i) + '\n')

    print(f.getvalue())
    response = HttpResponse(f.getvalue(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=file.txt'
    return render(request, "./crossword/result.html", {'matrix': generator_data["matrix"]})
