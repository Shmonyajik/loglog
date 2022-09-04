from django.db.models import Count
from django.contrib.auth.models import User,Group
from django.db.models import Q
# from .models import *

menu = [{'title': "", 'url_name': ''},
        {'title': "", 'url_name': ''},
        {'title': "", 'url_name': ''},
]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        group = Group.objects.get(name='ReadOnlyUsers')
        users = group.user_set.all()
        # group=Group(Q(name="Readonly") | Q(name="Readonly"))
        # users = User.objects.annotate(Count('is_superus'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            
        # user.groups.filter(name='Member').exists()
        # context['menu'] = user_menu

        # context['cats'] = cats
        context['users'] = users
        if 'user_selected' not in context:
            context['user_selected'] = 0
        return context
