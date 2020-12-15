from mongoengine import connect, disconnect

from openapi_server.dbmodels.organization import Organization
from openapi_server.dbmodels.person import Person
from openapi_server.dbmodels.tag import Tag
from openapi_server.dbmodels.grant import Grant


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_tag(tag_id):
    return Tag(tagId=tag_id).save()


def create_test_organization(organization_id):
    return Organization(
        organizationId=organization_id,
        name="Awesome Organization",
        shortName="AO",
        url="https://awesome-organization.org"
    ).save()


def create_test_person(organizations):
    return Person(
        firstName="Awesome",
        lastName="Person",
        email="awesome-person@example.org",
        organizations=organizations
    ).save()


def create_test_grant():
    return Grant(
        name="awesome-grant",
        description="description",
        url="https://report.nih.gov/"
    ).save()
