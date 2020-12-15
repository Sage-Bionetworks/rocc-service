from bson import ObjectId
from mongoengine import Document, StringField, EmailField, ListField, ObjectIdField, ReferenceField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class Person(Document):
    personId = ObjectIdField(primary_key=True, default=ObjectId)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    # TODO Decide whether email should be unique. If yes, email should be an
    # index
    email = EmailField()
    organizations = ListField(ReferenceField(Organization))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["personId"] = str(self.pk)
        return doc
