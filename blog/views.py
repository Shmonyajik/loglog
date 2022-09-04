
from multiprocessing import context
import operator
from django.utils.six.moves import reduce
from rest_framework import viewsets
from django.contrib.auth.models import User
from blog.documents import TjournalDocument
from blog.utils import DataMixin    
from django.shortcuts import render, redirect
from blog.serializers import  TjournalSerializer
from django.contrib.auth.views import LoginView
from core.forms import FiltersForm, LevelFilterForm, LoginUserForm 
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from elasticsearch_dsl.query import Q



class Filter(PermissionRequiredMixin,  View):
    permission_required = 'blog.view_tjournal'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')
    
    def get(self, request):
        if request.session:
            form = FiltersForm(request.session)                         
        else: form = FiltersForm()
        return render(request, 'filters.html', {'form': form})  
          
class Index(PermissionRequiredMixin,  View):
    serializer_class = TjournalSerializer
    document_class = TjournalDocument
    permission_required = 'blog.view_tjournal'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')
    def get(self, request):  
        journals = list(TjournalDocument.search()[:100])
        form = LevelFilterForm(request.GET)
        if form.is_valid():
            journals = TjournalDocument.search()[:100].execute()
        return render(request,"show.html",{'journals':journals, 'form': form}) 
    
    def post(self, request):
        #списки выбранных чекбоксов для формирования запроса
        levelRecordCheckbox = []
        EventCheckbox = []
        UserCheckbox = []
        ApplicationCheckbox = []
        ComputerCheckbox = []
        SessionCheckbox = []
        
        queries = [] # запрос к elasticsearch
        search = request.POST # словарь из постзапроса
        
        #выбранные  значения из чекбоксов
        event = search.getlist('Event')
        user = search.getlist('User')
        application= search.getlist('Application')
        computer = search.getlist('Computer')
        session = search.getlist('Session')
        
        
        print("search")
        print(search)
        #очистка сохраненных полей в сессии
        request.session['min_date'] = None
        request.session['max_date'] = None
        request.session['levelError'] = None
        request.session['levelWarning'] = None
        request.session['levelNote'] = None
        request.session['levelInfo'] = None
        request.session['Event'] = None
        request.session['User'] = None
        request.session['Application'] = None
        request.session['Computer'] = None
        request.session['Session'] = None
        request.session['MetaData'] = None
        request.session['DataRecord'] = None
        request.session['Datapresentation'] = None

        
        #Сохранение значений из формы в сессии
        ################################################################### 
        for item in search:
            if item != 'csrfmiddlewaretoken':
                if item =='Event'or item =='User' or item =='Application' or item =='Computer' or item =='Session':
                    request.session[item] = search.getlist(item)
                    print(request.session[item])
                else:
                    request.session[item] = search[item]
                    print(request.session[item])
        request.session.modified = True
        ###################################################################
       
        #Все значения поля [''] в Elasticsearch
        choices = tuple({x['Event'] for x in TjournalDocument.search()[:100].execute()})
        Users = tuple({x['User'] for x in TjournalDocument.search()[:100].execute()})
        Applications = tuple({x['Application'] for x in TjournalDocument.search()[:100].execute()})
        Computers = tuple({x['Computer'] for x in TjournalDocument.search()[:100].execute()})
        Sessions = tuple({x['Session'] for x in TjournalDocument.search()[:100].execute()})
        print("Session")
        print(Sessions)
        #Отбор списка значений по выбранному чекбоксу и полям события, пользователя, приложения, компьютера и сеанса
        for item in choices:
            if item in event:
                EventCheckbox.append(item)
        for item in Users :
            if item in user:
                UserCheckbox.append(item)
        for item in Applications:
            if item in application:
                ApplicationCheckbox.append(item)
        for item in Computers:
            if item in computer:
                ComputerCheckbox.append(item)
        for item in Sessions:
            if str(item) in session:
                SessionCheckbox.append(item)
        print("SessionCheckbox")
        print(SessionCheckbox)
        #Отбор списка значений по выбранному чекбоксу и  по полю Типа Данных
        if "levelError" in search:
            levelRecordCheckbox.append('Ошибка')
        if "levelWarning" in search:
            levelRecordCheckbox.append('Предупреждение')
        if "levelInfo" in search:
            levelRecordCheckbox.append('Информация')
        if "levelNote" in search:
            levelRecordCheckbox.append('Примечание')
        
        #Формирование запроса по Типу данных
        if(len(levelRecordCheckbox)>0):
            queries.append(Q(
                            'match_phrase', LevelRecord = levelRecordCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', LevelRecord = levelRecordCheckbox[1] if len(levelRecordCheckbox) >= 2 else levelRecordCheckbox[0]
                        )|
                        Q(
                            'match_phrase', LevelRecord = levelRecordCheckbox[2] if len(levelRecordCheckbox) >= 3 else levelRecordCheckbox[0]
                        )|
                        Q(
                            'match_phrase', LevelRecord = levelRecordCheckbox[3] if len(levelRecordCheckbox) >= 4 else levelRecordCheckbox[0]
                        )  
            ) 
        #формирование запроса по Событию
        if(len(EventCheckbox)>0):
            queries.append(Q(
                            'match_phrase', Event = EventCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', Event = EventCheckbox[1] if len(EventCheckbox) >= 2 else EventCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Event = EventCheckbox[2] if len(EventCheckbox) >= 3 else EventCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Event = EventCheckbox[3] if len(EventCheckbox) >= 4 else EventCheckbox[0]
                        )
                        
            ) 
        if(len(ApplicationCheckbox)>0):
            queries.append(Q(
                            'match_phrase', Application = ApplicationCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', Application = ApplicationCheckbox[1] if len(ApplicationCheckbox) >= 2 else ApplicationCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Application = ApplicationCheckbox[2] if len(ApplicationCheckbox) >= 3 else ApplicationCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Application = ApplicationCheckbox[3] if len(ApplicationCheckbox) >= 4 else ApplicationCheckbox[0]
                        )
                        
            ) 
        if(len(ComputerCheckbox)>0):
            queries.append(Q(
                            'match_phrase', Computer = ComputerCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', Computer = ComputerCheckbox[1] if len(ComputerCheckbox) >= 2 else ComputerCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Computer = ComputerCheckbox[2] if len(ComputerCheckbox) >= 3 else ComputerCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Computer = ComputerCheckbox[3] if len(ComputerCheckbox) >= 4 else ComputerCheckbox[0]
                        )
                        
            )
        if(len(UserCheckbox)>0):
            queries.append(Q(
                            'match_phrase', User = UserCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', User = UserCheckbox[1] if len(UserCheckbox) >= 2 else UserCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', User = UserCheckbox[2] if len(UserCheckbox) >= 3 else UserCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', User = UserCheckbox[3] if len(UserCheckbox) >= 4 else UserCheckbox[0]
                        )
                        
            )  
        if(len(SessionCheckbox)>0):
            queries.append(Q(
                            'match_phrase', Session = SessionCheckbox[0] 
                            )|
                        Q(
                            'match_phrase', Session = SessionCheckbox[1] if len(SessionCheckbox) >= 2 else SessionCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Session = SessionCheckbox[2] if len(SessionCheckbox) >= 3 else SessionCheckbox[0]
                        )
                        |
                        Q(
                            'match_phrase', Session = SessionCheckbox[3] if len(SessionCheckbox) >= 4 else SessionCheckbox[0]
                        )
                        
            )
         #Формирование запроса по дате
        if "min_date" in search:
            if search['min_date']:
                queries.append(Q(
                    'range',
                    DateRecord={'gte': search['min_date']}))
        if "max_date" in search:
            if search['max_date']:
                queries.append(Q( 
                    'range',
                    DateRecord={'lte': search['max_date']}))
        #Формирование запроса по данным
        if "MetaData" in search:
            if search['MetaData']:
                queries.append(Q('match', MetaData=str(search['MetaData'])))
        if "DataRecord" in search:
            if search['DataRecord']:
                queries.append(Q('match', DataRecord=str(search['DataRecord'])))
        if "DataPresentation" in search:
            if search['DataPresentation']:
                queries.append(Q('match', DataPresentationRecord=str(search['DataPresentation'])))
                
        print('meta')
        # print(search['Computer'])
        print("query")
        print(queries)
        if(queries):    
            journals = self.document_class.search()[:100].query(reduce(operator.iand, queries))
            serializer = self.serializer_class(journals, many=True)
            return render(request,"show.html",{'journals':serializer.data})
        else:
            return render(request,"show.html",{'journals':list(self.document_class.search()[:100])})
            
    
#administration VIEWS
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
    
def my_custom_permission_denied_view(request, exception):
     return render(request,'errs/403.html', status=403)


