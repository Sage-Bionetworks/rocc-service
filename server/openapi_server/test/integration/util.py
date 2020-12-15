from mongoengine import connect, disconnect

from openapi_server.dbmodels.tag import Tag
# from openapi_server.dbmodels.annotation_source import AnnotationSource
# from openapi_server.dbmodels.annotation_store import AnnotationStore
# from openapi_server.dbmodels.dataset import Dataset
# from openapi_server.dbmodels.fhir_store import FhirStore
# from openapi_server.dbmodels.note import Note
# from openapi_server.dbmodels.patient import Patient
# from openapi_server.dbmodels.resource_source import ResourceSource


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_tag(tag_id):
    return Tag(tagId=tag_id).save()
