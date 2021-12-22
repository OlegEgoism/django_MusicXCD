from django.shortcuts import render
from .models import Samples, Style, Format


def home(request):
    samples = Samples.objects.filter(published=True)
    context = {
        'samples': samples,
        'title': 'Семплы'
    }
    return render(request, template_name='home.html', context=context)






    # samples = Samples.objects.all()
    # res = '<h1>Список семплов</h1>'
    # for item in samples:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.authors}</p>\n<p>{item.format}</p>\n</div><hr>\n'
    # return HttpResponse(res)
