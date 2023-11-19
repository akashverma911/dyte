from django.shortcuts import render

# # Create your views here.
from django.http import JsonResponse
import requests
import json
from home.models import *

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def index(request):
    return JsonResponse({'status': 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        'level',
        'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata'
    )
    multi_match_search_fields = (
        'level',
        'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata'
    )
    filter_fields = {
        'level':'level',
        'message':'message',
        'resourceId':'resourceId',
        'timestamp':'timestamp',
        'traceId':'traceId',
        'spanId':'spanId',
        'commit':'commit',
        'metadata':'metadata'
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ('id',)



