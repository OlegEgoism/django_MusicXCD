from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import *


class AddAuthorForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Добавить автора', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Добавьте автора если такого нет в списке'}))

    class Meta:
        model = Author
        fields = ['name']


def validator_size(value):
    if value <= 0:
        raise ValidationError('Размер файла не может быть отрицательным')


class SamplesForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),
                                            label='Автор (выберетеи одного или нескольких авторов из списка)',
                                            widget=forms.CheckboxSelectMultiple)
    style = forms.ModelMultipleChoiceField(queryset=Style.objects.all(),
                                           label='Стиль (выберите один или несколько стилей из списка)',
                                           widget=forms.CheckboxSelectMultiple)
    format = forms.ModelMultipleChoiceField(queryset=Format.objects.all(),
                                            label='Формат (выберите один или несколько форматов из списка)',
                                            widget=forms.CheckboxSelectMultiple)
    title = forms.CharField(max_length=100, label='Название библиотекеи семплов', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Укажите польное имя вашей библиотеки семплов'}))
    descriptions = forms.CharField(label='Описание библиотекеи семплов', required=False, widget=forms.Textarea(
        attrs={'style': 'margin:10px; padding:10px; height:140px', 'class': 'form-control col-sm-8',
               'placeholder': 'Укажите полное описание вашей библиотеки сэмплов без ссылок на стороннии источники'}))
    photo = forms.ImageField(label='Обложка', required=False)
    size = forms.DecimalField(label='Размер файла', validators=[validator_size], widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Укажите размер файла в мегабайтах (Mbyte, MB)'}))
    link = forms.CharField(label='Ссылка для скачивания', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Укажите полную ссылку для скачивания файла'}))

    class Meta:
        model = Samples
        fields = ['author', 'style', 'format', 'title', 'descriptions', 'photo', 'size', 'link']


def password(value):
    if len(value) < 5:
        raise ValidationError('Пароль должен содержать не меньше 5 символов')


class UserRegistrationForm(forms.ModelForm):  # UserCreationForm #forms.Form
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Напишите свой логин'}))
    password1 = forms.CharField(label='Пароль', validators=[password], widget=forms.PasswordInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Введите пароль не мение 5 символов'}))
    password2 = forms.CharField(label='Пароль (подтверждение)', validators=[password], widget=forms.PasswordInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Введите пароль не мение 5 символов'}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Электронная почта (e-mail)'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Номер телефона с кодом страны'}))
    capthca = CaptchaField(label='')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'phone')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль не совпадает')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Этот почтовый адрес уже зарегистрирован')


class UserLoginForm(AuthenticationForm):  # AuthenticationForm #forms.Form
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Напишите свой логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Введите пароль не мение 5 символов'}))


class EmailForm(forms.Form):
    subject = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'style': 'margin:10px; padding:10px; height:40px', 'class': 'form-control col-sm-8',
               'placeholder': 'Напишите вашу почту'}))
    content = forms.CharField(label='Текст письма', widget=forms.Textarea(
        attrs={'style': 'margin:10px; padding:10px; height:200px', 'class': 'form-control col-sm-8',
               'placeholder': 'Напишите текст письма'}))
    capthca = CaptchaField(label='')

    # phone = forms.CharField(label='Мобильный телефон', help_text='(телефон с кодом страны)', widget=forms.TextInput)
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Пароль подтверждения', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    # fields = ('username', 'first_name', 'last_name')
    # widgets = {
    #     'email': forms.TextInput(attrs={'style': 'margin:10px; padding:10px;height:40px', 'class': 'form-control col-sm-8', 'placeholder': 'E-mail please'}),

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password1'] != cd['password2']:
    #         raise forms.ValidationError('Пароль не совпадает')
    #     return cd['password2']
    #

    #
    # class Meta:
    #     model = User()
    #     fields = ('email', 'lastname', 'firstname')
    #     widgets = {
    #         'email': forms.TextInput(attrs={'style': 'margin:10px; padding:10px;height:40px', 'class': 'form-control col-sm-8', 'placeholder': 'E-mail please'}),
    #         'lastname': forms.TextInput(attrs={
    #             'style': 'margin:10px; padding:10px;height:40px',
    #             'class': 'form-control col-sm-8',
    #             'placeholder': 'Lastname please'
    #         }),
    #         'firstname': forms.TextInput(attrs={
    #             'style': 'margin:10px; padding:10px;height:40px',
    #             'class': 'form-control col-sm-8',
    #             'placeholder': 'Firstname please'
    #         }),
    #     }

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(
#         label='passwd',
#         widget=forms.PasswordInput(attrs={
#             'style': 'margin:10px; padding:10px;height:40px',
#             'class': 'form-control col-sm-8',
#             'placeholder': 'Password please'
#         })
#     )
#     password2 = forms.CharField(
#         label='double passwd',
#         widget=forms.PasswordInput(attrs={
#             'style': 'margin:10px; padding:10px;height:40px',
#             'class': 'form-control col-sm-8',
#             'placeholder': 'Double password please'
#         })
#     )
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwd and double passwd error')
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(
#             self.cleaned_data['password1'])  # важно тут передавать password1 или 2. Но не password как в примере выше
#         if commit:
#             user.save()
#         return user
#


#     class Meta:
#         model = User()
#         fields = ('email', 'lastname', 'firstname')
#         widgets = {
#             'email': forms.TextInput(attrs={
#                 'style': 'margin:10px; padding:10px;height:40px',
#                 'class': 'form-control col-sm-8',
#                 'placeholder': 'E-mail please'
#             }),
#             'lastname': forms.TextInput(attrs={
#                 'style': 'margin:10px; padding:10px;height:40px',
#                 'class': 'form-control col-sm-8',
#                 'placeholder': 'Lastname please'
#             }),
#             'firstname': forms.TextInput(attrs={
#                 'style': 'margin:10px; padding:10px;height:40px',
#                 'class': 'form-control col-sm-8',
#                 'placeholder': 'Firstname please'
#             }),
#         }


# def clean(self):
#     cleaned_data = super().clean(self)
#     if User.objects.filter(email=cleaned_data.get('email')).exists():
#         self.fields.add_error('email', "Эта почта уже зарегестрированна")
#     return cleaned_data


# class Meta:
#     model = User
#     fields = ('username', 'first_name', 'last_name', 'email')
#
# def clean_password2(self):
#     cd = self.cleaned_data
#     if cd['password'] != cd['password2']:
#         raise forms.ValidationError('Пароль не совпадает')
#     return cd['password2']

#


#
# class Meta:
#     model = User
#     fields = ('username', 'first_name', 'last_name', 'email')
#
# def clean_password2(self):
#     cd = self.cleaned_data
#     if cd['password'] != cd['password2']:
#         raise forms.ValidationError('Пароль не совпадает')
#     return cd['password2']

# class RegisterUserForm(UserCreationForm): #(forms) (ModelForm)
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
