from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import *
# import re

class AddAuthorForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Новый автор (добавьте автора если такого нет в списке)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Author
        fields = ['name']


def validator_size(value):
    if value < 0:
        raise ValidationError('Размер файла не может быть отрицательным')


class SamplesForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автор (выберетеи одного или нескольких авторов из списка)', widget=forms.CheckboxSelectMultiple)
    style = forms.ModelMultipleChoiceField(queryset=Style.objects.all(), label='Стиль (выберите один или несколько стилей из списка)', widget=forms.CheckboxSelectMultiple)
    format = forms.ModelMultipleChoiceField(queryset=Format.objects.all(), label='Формат (выберите один или несколько форматов из списка)', widget=forms.CheckboxSelectMultiple)
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    photo = forms.ImageField(label='Обложка', required=False)
    size = forms.DecimalField(label='Размер в МБ (напишите размер файла числом через точку)', validators=[validator_size], widget=forms.TextInput(attrs={'class': 'form-control'}))
    link = forms.CharField(label='Ссылка для скачивания', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Samples
        fields = ['author', 'style', 'format', 'title', 'descriptions', 'photo', 'size', 'link']


class RegisterUserForm(UserCreationForm): #(forms) (ModelForm)
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
















    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 10:
    #         raise ValidationError('Длина привышает 10 символов')
    #     return title



    # def validator_size(value):
    #     if value <= 0:
    #         raise ValidationError('Размер не может быть отрицательный')





    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if re.match(r'\d', title):
    #         raise ValidationError('Название должно начинаться с буквы')
    #     return title

    # class AddAuthorForm(UserCreationForm):
    #     class Meta:
    #         model = Author
    #         fields = ['name']
    #
    #     def clean(self):
    #         cleaned_data = super().clean(self)
    #         if Author.objects.filter(email=cleaned_data.get('email')).exists():
    #             self.fields.add_error('email', "Эта почта уже зарегестрированна")
    #         return cleaned_data








    # def clean_author(self):
    #     data = self.cleaned_data['author']
    #     if "Egoism" not in data:
    #         raise forms.ValidationError("Такой автор уже есть в базе")
    #     return data
    #     if Author.objects.filter(name=self.cleaned_data['name']).exists():

    # def clean_author(self):
    #     author = self.cleaned_data['author']
    #     if author != author:
    #         raise ValidationError('Такой  автор есть')
    #     return author

    # def clean_author(self):
    #     print(type(self.cleaned_data))
    #     author = self.cleaned_data.get('author')
    #     if author != author:
    #         raise ValidationError('Такой  автор есть')
    #     return author




# def user_cap(name):
#     if name.isupper():
#         raise ValidationError('Имя с большой буквы')
#     else:
#         return
# class RegisterUserForm(UserCreationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#
# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#
# class FormUserView(forms.Form):
#     author = forms.CharField(max_length=150, label='Author name', validators=[user_cap], help_text='Имя с большой буквы и не мение 5 символов')
#     style = forms.CharField(max_length=150, label='Style name', validators=[user_cap], help_text='Имя с большой буквы и не мение 5 символов')
#     format = forms.CharField(max_length=150, label='Format name', validators=[user_cap], help_text='Имя с большой буквы и не мение 5 символов')
#     title = forms.CharField(max_length=150, label='Note', help_text='Поле не должно быть пустым')
#     descriptions = forms.CharField(max_length=150, label='Note', help_text='Поле не должно быть пустым')
#     size = forms.CharField(max_length=150, label='Note', help_text='Поле не должно быть пустым')
#     photo = forms.CharField(max_length=150, label='Note', help_text='Выберите файл нужного формата')
#     link = forms.CharField(max_length=150, label='Note', help_text='Поле не должно быть пустым')
#







