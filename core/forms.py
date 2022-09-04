from email.mime import application
from importlib.resources import path
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import  AuthenticationForm
from blog.documents import TjournalDocument
from blog.models import Tjournal


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
class DateFilterForm(forms.Form):
    min_date = forms.CharField(label='От', widget=forms.TextInput(attrs={'class': 'form-input'}))
    max_date = forms.CharField(label='До', widget=forms.TextInput(attrs={'class': 'form-input'}))
class LevelFilterForm(forms.Form):
    level = forms.CharField(label='Тип данных', widget=forms.TextInput(attrs={'class': 'form-input'}))
class FiltersForm(forms.Form):
    min_date = forms.DateTimeField(label='От',required= False, widget=forms.DateTimeInput(attrs={'class': 'form-input'}))
    max_date = forms.DateTimeField(label='До',required= False, widget=forms.DateTimeInput(attrs={'class': 'form-input'}))
    levelError = forms.BooleanField(label='Ошибка', required=False)
    levelWarning = forms.BooleanField(label='Предупреждение', required=False)
    levelInfo = forms.BooleanField(label='Информация', required=False)
    levelNote = forms.BooleanField(label='Примечание', required=False)
    MetaData = forms.CharField(label='Метаданные', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    DataRecord = forms.CharField(label='Данные', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    DataPresentation = forms.CharField(label='Представление данных', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    choices = tuple({x['Event'] for x in TjournalDocument.search()[:100].execute()})
    Event = forms.ChoiceField(label='События', choices=(*zip(choices, choices),)
    , widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input'}))
    
    choices = tuple({x['User'] for x in TjournalDocument.search()[:100].execute()})
    User = forms.ChoiceField(label='Пользователи', choices=(*zip(choices, choices),)
    , widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input'}))
    
    choices = tuple({x['Application'] for x in TjournalDocument.search()[:100].execute()})
    Application = forms.ChoiceField(label='Приложения', choices=(*zip(choices, choices),)
    , widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input'}))
    
    choices = tuple({x['Computer'] for x in TjournalDocument.search()[:100].execute()})
    Computer = forms.ChoiceField(label='Компьютеры', choices=(*zip(choices, choices),)
    , widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input'}))
    
    choices = tuple({x['Session'] for x in TjournalDocument.search()[:100].execute()})
    Session = forms.ChoiceField(label='Сеансы', choices=(*zip(choices, choices),)
    , widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input'}))
    
    

   
    # Users = tuple({x['User'] for x in TjournalDocument.search().execute()})
    # Applications = tuple({x['Application'] for x in TjournalDocument.search().execute()})
    # Computers = tuple({x['Computer'] for x in TjournalDocument.search().execute()})
    # Sessions = tuple({x['Session'] for x in TjournalDocument.search().execute()})
    
    
    
    
