from django.contrib.auth.models import User
from django.db import models

class Tjournal(models.Model):
    DataBase = models.CharField(max_length=256)
    LevelRecord = models.CharField(max_length=256, blank = True)
    DateRecord = models.DateTimeField(blank = True, null=True)
    Application = models.CharField(max_length=256, blank = True)
    Computer = models.TextField(max_length=256, blank = True)
    Event = models.TextField(max_length=256)
    Comment = models.TextField(max_length=256, blank = True)
    MetaData = models.TextField(max_length=256, blank = True)
    DataRecord = models.TextField(max_length=256, blank = True)
    DataPresentationRecord = models.TextField(max_length=256, blank = True)
    ApplicationPresentation = models.TextField(max_length=256, blank = True)
    EventPresentation = models.TextField(max_length=256, blank = True)
    MetaDataPresentation = models.TextField(max_length=256, blank = True)
    Transaction_status = models.CharField(max_length=256, blank = True)
    Transaction_id = models.TextField(max_length=256, blank = True)
    Session = models.SmallIntegerField(blank = True,null=True)
    Connection = models.IntegerField(blank = True,null=True)
    ServerName = models.CharField(max_length=256, blank = True)
    Port = models.SmallIntegerField(blank = True,null=True)
    SyncPort = models.TextField(max_length=256, blank = True)
    SessionDataSeparation = models.TextField(max_length=256, blank = True)
    SessionDataSeparationPresentation = models.TextField(max_length=256, blank = True)
    User = models.CharField(max_length=256, blank = True)
    UidUse = models.CharField(max_length=256, blank = True)
    UserName = models.CharField(max_length=256, blank = True)
    
    class Meta:
        verbose_name_plural = 'Tjournals'

    def __str__(self):
        return f'{self.Event}'
    
  
      