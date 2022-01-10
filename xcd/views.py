from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import SamplesForm, AddAuthorForm, LoginUserForm, RegisterUserForm
from django.views.generic import CreateView, ListView
from django.http import HttpResponse

#Новые добавления
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy




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


def get_style(request, slug):
    samples = Samples.objects.filter(style__slug=slug, published=True)
    get_object_or_404(Style, slug=slug)
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Семплы',
        'samples': samples,
        'style': style,
        'author': author,
    }
    return render(request, template_name='home.html', context=context)


def get_author(request, slug):
    samples = Samples.objects.filter(author__slug=slug, published=True)
    get_object_or_404(Author, slug=slug)
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
            # return redirect('add_samples')
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
            return redirect('published')  #Куда перейдем после добавления
    else:
        form = SamplesForm() #Если проверка выше не прошла
    context = {
        'title': 'Добавить семплы',
        'style': style,
        'author': author,
        'form': form,
        'form_a': form_a,
    }
    return render(request, template_name='add_samples.html', context=context)


def add_published(request):
    style = Style.objects.all()
    author = Author.objects.all()
    context = {
        'title': 'Опубликовано',
        'style': style,
        'author': author,
    }
    return render(request, template_name='published_samples.html', context=context)


# AWe#

class RegisterUser(CreateView):
    style = Style.objects.all()
    author = Author.objects.all()
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    context = {
        'title': 'Опубликовано',
        'style': style,
        'author': author,
    }
    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    # return render(request, template_name='register.html', context=context)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')




# from django.contrib.auth import authenticate, login
#
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...



# def search(request):
#     style = Style.objects.all()
#     author = Author.objects.all()
#     sea = request.GET.get('sea')
#     if request.method =='POST':
#         if sea in request.GET:
#             return HttpResponse('Мы нашли' % request.POST['sea'])
#         else:
#             return HttpResponse('Вы отправили пустой завпрос')
#     context = {
#         'title': 'Опубликовано',
#         'style': style,
#         'author': author,
#     }
#     return render(request, template_name='search.html', context=context)

def search(request):
    str_search = request.GET.get('search')
    if str_search:
        list_search = str_search.split()
        res = []
        for i in list_search:
            authors = Author.objects.filter(name__icontains=i).first()
            descriptions = Samples.objects
            # print(authors)
            # if authors:
            #     authors = Author.objects.filter(name__icontains=i)
            res.append(authors)
            #     print(res)
            # else:
            #     print('No')
    return render(request, template_name='search.html', context={'authors':res})


    #
    # if request.GET.get("q") != None:
    #     query = request.GET.get("q")
    #     context["array"] = Samples.objects.filter(DB__item__contains=query)
    # print(request.GET.get('search'))



# class Search(ListView):
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Samples.objects.filter(name__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["q"] = f'q={self.request.GET.get("q")}&'
#         return context



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
