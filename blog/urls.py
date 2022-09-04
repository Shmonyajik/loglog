from django.urls import path, include
from rest_framework import routers

from blog.views import  LoginUser, Filter

router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'tjournal', TjournalViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginUser.as_view(), name='login'),
    path('filter/', Filter.as_view(), name='filter'),
   
]
