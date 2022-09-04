
from django.urls import path

from search.views import  FilterDateTjournals, SearchTjournals, SearchUsers,  FilterTjournals

urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('filter/', FilterTjournals.as_view()),
    path('filterDate/', FilterDateTjournals.as_view()),
    path('tjournal/<str:query>/', SearchTjournals.as_view()),
    #path('tabletjournal/', TableTjournal.as_view()),
    
    
]
