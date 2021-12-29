from django.shortcuts import render
from .models import Samples, Style, Author
from django.http import HttpResponse

def home(request):
    samples = Samples.objects.filter(published=True)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='home.html', context=context)


def get_style(request, name):
    samples = Samples.objects.filter(style__id=name, published=True)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='home.html', context=context)


def get_author(request, name):
    samples = Samples.objects.filter(author__id=name, published=True)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='home.html', context=context)


def get_info(request, pk):
    samples = Samples.objects.filter(id=pk, published=True)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Информация',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='info.html', context=context)





#
# def get_info(request):
#     return HttpResponse("hi Oleg")


    # samples = Samples.objects.filter(author__id=name, published=True)
    # style = Style.objects.all()
    # author = Author.objects.all()
    # context = {
    #     'title': 'Информация',
    #     'samples': samples,
    #     'style': style,
    #     'author': author,
    # }
    # return render(request, template_name='info.html', context=context)






    # authors = Samples.objects.values_list('authors').order_by('authors').distinct()
    # for authors in Samples.objects.values_list('authors', flat=True).distinct():
    #     Samples.objects.filter(pk__in=Samples.objects.filter(authors=authors).values_list('id', flat=True)[1:])
    #     print(authors)

    # style = Style.objects.get(id=id)
    # # print(styles)
    # samples = Samples.objects.filter(style=style)
    # styless = Style.objects.get(name=id)

    # samples = Samples.objects.all()

