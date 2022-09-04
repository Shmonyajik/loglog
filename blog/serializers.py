from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import  Tjournal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


        
class TjournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tjournal
        fields = ('__all__')
