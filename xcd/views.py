from django.shortcuts import render
from .models import Samples, Style, Format


def home(request):
    samples = Samples.objects.filter(published=True)
    style = Style.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
    }
    return render(request, template_name='home.html', context=context)


def get_style(request, id):

    # style = Style.objects.get(id=id)
    # # print(styles)
    # samples = Samples.objects.filter(style=style)
    samples = Samples.objects.filter(style__id=id)

    styles = Style.objects.all()
    # styless = Style.objects.get(name=id)
    context = {
        'samples': samples,
        'styles': styles,
        # 'styless': styless,
    }
    return render(request, 'style.html', context=context)












    # samples = Samples.objects.all()
    # res = '<h1>Список семплов</h1>'
    # for item in samples:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.authors}</p>\n<p>{item.format}</p>\n</div><hr>\n'
    # return HttpResponse(res)
