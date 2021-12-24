from django.shortcuts import render
from .models import Samples, Style, Format, Author


def home(request):
    samples = Samples.objects.filter(published=True)
    style = Style.objects.all()
    authors = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'authors': authors,
    }
    return render(request, template_name='home.html', context=context)


def get_style(request, name):
    samples = Samples.objects.filter(style__id=name, published=True)
    style = Style.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
    }
    return render(request, 'style.html', context=context)



    # authors = Samples.objects.values_list('authors').order_by('authors').distinct()
    # for authors in Samples.objects.values_list('authors', flat=True).distinct():
    #     Samples.objects.filter(pk__in=Samples.objects.filter(authors=authors).values_list('id', flat=True)[1:])
    #     print(authors)








    # style = Style.objects.get(id=id)
    # # print(styles)
    # samples = Samples.objects.filter(style=style)
    # styless = Style.objects.get(name=id)

    # samples = Samples.objects.all()
    # res = '<h1>Список семплов</h1>'
    # for item in samples:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.authors}</p>\n<p>{item.format}</p>\n</div><hr>\n'
    # return HttpResponse(res)
