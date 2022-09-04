from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
]

#new
urlpatterns+=[   
    # path('', views.index, name='home'),  
    path('', views.Index.as_view(), name='home'),       
]  
handler403 = 'blog.views.my_custom_permission_denied_view'