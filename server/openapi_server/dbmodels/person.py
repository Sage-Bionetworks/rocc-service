from mongoengine import Document, StringField, EmailField, ListField, ObjectIdField, ReferenceField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class Person(Document):
    personId = ObjectIdField(required=False, primary_key=True)
    firstName = StringField(min_length=1)
    lastName = StringField(min_length=1)
    email = EmailField()
    organizations = ListField(ReferenceField(Organization))  # XXX Difference with StringField?  # noqa: E501

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["personId"] = str(self.pk)
        return doc
