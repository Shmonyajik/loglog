from dataclasses import field
from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from blog.models import Tjournal

@registry.register_document
class TjournalDocument(Document):
    
    class Index:
        name = 'tjournal'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 1,
        }

    class Django:
        model = Tjournal
        fields = [
            'DataBase', 
            'LevelRecord', 
            'DateRecord',
            'Application' ,
            'Computer' ,
            'Event',
            'Comment' ,
            'MetaData' ,
            'DataRecord' ,
            'DataPresentationRecord' ,
            'ApplicationPresentation' ,
            'EventPresentation' ,
            'MetaDataPresentation' ,
            'Transaction_status' ,
            'Transaction_id',
            'Session' ,
            'Connection' ,
            'ServerName',
            'Port',
            'SyncPort',
            'SessionDataSeparation', 
            'SessionDataSeparationPresentation' ,
            'User' ,
            'UidUse' ,
            'UserName' 
        ]

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]


