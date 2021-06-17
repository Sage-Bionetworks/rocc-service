from bson import ObjectId
from mongoengine import Document, StringField, EmailField, ListField, ObjectIdField, ReferenceField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class Person(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    email = EmailField()  # TODO: maybe make unique again later?
    organizationIds = ListField(ReferenceField(Organization), required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        return doc
