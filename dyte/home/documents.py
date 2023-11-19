from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from .models import ElasticDemo
PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr='id')
    fielddata = True
    level = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    message = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    resourceId = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    timestamp = fields.DateField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    traceId = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    spanId = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    commit = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    metadata = fields.ObjectField(properties={
        'parentResourceId': fields.TextField(),
    })
    class Django(object):
        model = ElasticDemo
        
