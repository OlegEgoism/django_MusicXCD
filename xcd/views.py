from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from .models import *
from .forms import SamplesForm, AddAuthorForm
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


def get_style(request, pk):
    samples = Samples.objects.filter(style__id=pk, published=True)
    get_object_or_404(Style, pk=pk)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='home.html', context=context)


def get_author(request, pk):
    samples = Samples.objects.filter(author__id=pk, published=True)
    get_object_or_404(Author, pk=pk)
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
    get_object_or_404(Samples, pk=pk)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Информация',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='info.html', context=context)



def add_author(request):
    style = Style.objects.all()
    author = Author.objects.all()
    if request.method == 'POST':
        form_a = AddAuthorForm(request.POST)
        if form_a.is_valid():
            form_a.save()
    context = {
        'title': 'Добавить автора',
        'style': style,
        'author': author,
    }
    return render(request, template_name='published_author.html', context=context)


def add_samples(request):
    style = Style.objects.all()
    author = Author.objects.all()
    form_a = AddAuthorForm()
    if request.method == 'POST':
        form = SamplesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('published')  # куда перейдем после добавления
    else:
        form = SamplesForm()
    context = {
        'title': 'Добавить семплы',
        'style': style,
        'author': author,
        'form': form,
        'form_a':form_a

    }
    return render(request, template_name='add_samples.html', context=context)


def add_ok(request):
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Опубликовано',
        'style': style,
        'author': author,
    }
    return render(request, template_name='published_samples.html', context=context)

# def add_ok(request):
#     style = Style.objects.all()
#     author = Author.objects.all()
#     context = {
#         'title': 'Cемплы добавлины',
#         'style': style,
#         'author': author,
#     }
#     return HttpResponse("Спасибо все хорошо")


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
