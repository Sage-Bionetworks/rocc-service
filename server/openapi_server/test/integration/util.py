from mongoengine import connect, disconnect

from openapi_server.dbmodels.organization import Organization
from openapi_server.dbmodels.tag import Tag


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_tag(tag_id):
    return Tag(tagId=tag_id).save()


def create_test_organization(organization_id):
    return Organization(
        organizationId=organization_id,
        name="Sage Bionetworks",
        shortName="Sage",
        url="https://openapi-generator.tech"
    ).save()
