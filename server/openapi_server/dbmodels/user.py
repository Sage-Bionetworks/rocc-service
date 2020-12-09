from mongoengine import Document, ListField, ReferenceField, StringField, EmailField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class User(Document):
    username = StringField(required=True)
    password = StringField(min_length=3)
    firstName = StringField(min_length=1)
    lastName = StringField(min_length=1)
    email = EmailField(required=True)
    role = StringField(choices=["user", "admin"], default="admin")
    organizations = ListField(ReferenceField(Organization))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)
        return doc
