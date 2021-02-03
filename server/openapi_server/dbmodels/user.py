from mongoengine import Document, StringField, EmailField, ListField, ReferenceField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class User(Document):
    username = StringField(primary_key=True)
    # password = StringField(required=True)
    role = StringField(choices=["user", "admin"], default="user")
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    email = EmailField()  # TODO: maybe make unique again later?
    organizations = ListField(ReferenceField(Organization))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['username'] = str(self.pk)
        doc.pop('_id', None)
        # doc.pop('password', None)
        return doc
