import abc

from django.http import HttpResponse
from core.forms import DateFilterForm, LevelFilterForm
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import View
from blog.documents import  UserDocument,  TjournalDocument
from blog.serializers import  UserSerializer,  TjournalSerializer
from elasticsearch import Elasticsearch


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query,request)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)
        
class SearchTjournals(PaginatedElasticSearchAPIView):
    serializer_class = TjournalSerializer
    document_class = TjournalDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'Event',
                    'DataBase',
                    'User',
                ], fuzziness='auto')

# class FilterTjournal():
#     serializer_class = TjournalSerializer
#     document_class = TjournalDocument
#     def get(self,request):
#         try:           
#             form = DateFilterForm(request.GET)
#             if form.is_valid():
#                 search = self.document_class.search().query(
#                     Q('range', DateRecord={'gte',form.cleaned_data["min_date"]}) &
#                     Q('range', DateRecord={'lte',form.cleaned_data["max_date"]})
#                     )
#             response = search.execute()
#             #print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

#             # results = self.paginate_queryset(response, request, view=self)
#             serializer = self.serializer_class(response, many=True)
#             return render(request,"show.html",{'journals':serializer.data, 'form': form}) 
#             # return self.get_paginated_response(serializer.data)
#         except Exception as e:
#             return HttpResponse(e, status=500)
# views

# class TableTjournal(PaginatedElasticSearchAPIView):
#     serializer_class = TjournalSerializer
#     document_class = TjournalDocument
#     def get(self, request):
#         try:
#             q = 
#             search = self.document_class.search(index='tjournal')
#             response = search.execute()

#             #print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

#             results = self.paginate_queryset(response, request, view=self)
#             serializer = self.serializer_class(results, many=True)
#             return self.get_paginated_response(serializer.data)
#         except Exception as e:
#             return HttpResponse(e, status=500)
        
        
# class FilterTjournals(APIView,View):
#     serializer_class = TjournalSerializer
#     document_class = TjournalDocument
#     def get(self, request):
#         # try: 
#         es = Elasticsearch()
#         journals = list(TjournalDocument.search())
#         form = LevelFilterForm(request.GET) 
#         if form.is_valid():
#                 search_param = {
#                     'query': {
#                         'match': {
#                             'Event': "Изменение"
#                         }
#                     }
#                 }
#                 search = es.Search(index = "tjournal", body = search_param)
#                 response = search.execute()
#                 # results = self.queryset(response, request, view=self)
#                 serializer = self.serializer_class(response, many=True)
#                 return render(request,"show.html",{'journals':serializer.data, 'form': form})
#         return render(request,"show.html",{'journals':journals, 'form': form})
        
# class FilterDateTjournals(APIView,View):
#     serializer_class = TjournalSerializer
#     document_class = TjournalDocument
    
#     def get(self, request):
#         # try: 
#         journals = list(TjournalDocument.search())
#         form = DateFilterForm(request.GET) 
#         if form.is_valid():
#                 q = (
#                     Q('match', DateRecord = str(form.cleaned_data["min_date"]))
#                     )
#                 search = self.document_class.search().query(q)
#                 response = search.execute()
#                 # results = self.queryset(response, request, view=self)
#                 serializer = self.serializer_class(response, many=True)
#                 return render(request,"show.html",{'journals':serializer.data, 'form': form})
#         return render(request,"show.html",{'journals':journals, 'form': form})
    
    
    
class FilterTjournals(View):
    serializer_class = TjournalSerializer
    document_class = TjournalDocument
    def get(self, request):
        # try: 
        es = Elasticsearch()
        journals = list(TjournalDocument.search())
        form = LevelFilterForm(request.GET) 
        if form.is_valid():
                q = (
                    Q('match', LevelRecord = str(form.cleaned_data["level"]))
                    )
                search = self.document_class.search().query(q)
                response = search.execute()
                # results = self.queryset(response, request, view=self)
                serializer = self.serializer_class(response, many=True)
                return render(request,"show.html",{'journals':serializer.data, 'form': form})
        return render(request,"show.html",{'journals':journals, 'form': form})
        
class FilterDateTjournals(APIView,View):
    serializer_class = TjournalSerializer
    document_class = TjournalDocument
    
    def get(self, request):
        # try: 
        journals = list(TjournalDocument.search())
        form = DateFilterForm(request.GET) 
        if form.is_valid():
                # q = (
                #     Q('range', Port = str({'gte',form.cleaned_data["min_date"]}))&
                #     Q('range', Port = str({'lte',form.cleaned_data["max_date"]}))
                #     )
                search = self.document_class.search().filter('range', DateRecord={'gte': form.cleaned_data["min_date"], 'lte': form.cleaned_data["max_date"]}).execute()
                # search = search.search().filter('range', Port = {'lte',form.cleaned_data["max_date"]})
                # response = search.execute()
                # results = self.queryset(response, request, view=self)
                serializer = self.serializer_class(search, many=True)
                return render(request,"show.html",{'journals':serializer.data, 'form': form})
        return render(request,"show.html",{'journals':journals, 'form': form})
    
    
    
        # except Exception as e:
        #     return HttpResponse(e, status=500)
                
    # def generate_q_expression(self,  request):
    #     form = DateFilterForm(request.GET)
    #     return query(
    #                 Q('range', DateRecord={'gte',form.cleaned_data["min_date"]}) &
    #                 Q('range', DateRecord={'lte',form.cleaned_data["max_date"]})
    #                 )
    # def get(self, request):  
    #         q = self.generate_q_expression(request)
    #         search = self.document_class.search().query(q)
    #         response = search.execute()

    #         print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

    #         results = self.paginate_queryset(response, request, view=self)
    #         serializer = self.serializer_class(results, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     # journals = list(TjournalDocument.search())
        
    #     # form = DateFilterForm(request.GET)
    #     # if form.is_valid():
    #     #     journals = TjournalDocument.search().filter('range', DataRecord = {'gte', "2000-01-01T00:00:00"})
    #     #     # journals = list(TjournalDocument.search().query(
    #     #     #     Q('range', DateRecord={'gte',form.cleaned_data["min_date"]}) &
    #     #     #     Q('range', DateRecord={'lte',form.cleaned_data["max_date"]})
    #     #     # )).execute()
    #     # #     filter('range', DateRecord={'gte',form.cleaned_data["min_date"]})
    #     # # if form.is_valid():
    #     # #     journals = journals.search().filter('range', DateRecord={'lte',form.cleaned_data["max_date"]})
    #     return render(request,"show.html",{'journals':journals, 'form': form})    
    

class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', username=query),
                     Q('match', first_name=query),
                     Q('match', last_name=query),
                 ], minimum_should_match=1)

