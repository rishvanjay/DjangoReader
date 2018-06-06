# api/resources.py
from tastypie.resources import ModelResource
from api.models import Read
from tastypie.authorization import Authorization

class ReadResource(ModelResource):
    class Meta:
        queryset = Read.objects.all()
        resource_name = 'read'
        authorization = Authorization()
        fields = ['url', 'html']