from django.core.exceptions import ValidationError
from django import forms
from .models import *

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    # author = forms.CharField(label='Авторы')


class SamplesForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автор', widget=forms.CheckboxSelectMultiple)
    style = forms.ModelMultipleChoiceField(queryset=Style.objects.all(), label='Стиль', widget=forms.CheckboxSelectMultiple)
    format = forms.ModelMultipleChoiceField(queryset=Format.objects.all(), label='Формат', widget=forms.CheckboxSelectMultiple)
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descriptions = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    photo = forms.ImageField(label='Обложка', required=False)
    size = forms.CharField(label='Размер в МБ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    link = forms.CharField(label='Ссылка для скачивания', widget=forms.TextInput(attrs={'class': 'form-control'}))
    published = forms.BooleanField(label='Опубликовать?', initial=True)
    class Meta:
        model = Samples
        fields = '__all__'



# class SamplesForm(forms.Form):
#     author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автор')
#     style = forms.ModelMultipleChoiceField(queryset=Style.objects.all(), label='Стиль', widget=forms.CheckboxSelectMultiple)
#     format = forms.ModelMultipleChoiceField(queryset=Format.objects.all(), label='Формат', widget=forms.CheckboxSelectMultiple)
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     descriptions = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#     photo = forms.ImageField(label='Обложка', required=False)
#     size = forms.CharField(label='Размер в МБ', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     link = forms.CharField(label='Ссылка для скачивания', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     published = forms.BooleanField(label='Опубликовать?', initial=True)



#
# def user_cap(name):
#     if name.isupper():
#         raise ValidationError('Имя с большой буквы')
#     elif len(name) < 5:
#         raise ValidationError('Имя не менее 5 букв')
#     else:
#         return
#
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







#
# from .models import Owner, Book, Store, Author
#
#
# class StoreForm(forms.ModelForm):
#     class Meta:
#         model = Owner
#         fields = ['name']
#
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# class GetPost(forms.Form):
#     name = forms.CharField(max_length=50)
#     pages = forms.IntegerField()
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
