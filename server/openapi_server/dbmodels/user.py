from mongoengine import StringField, EmailField

from openapi_server.dbmodels.organization import Organization


class Challenge(Document):
    username = StringField(required=True)
    password = StringField()
    firstName = StringField()
    lastName = StringField()
    email = EmailField()
    role = StringField
    organizations = ListField(ReferenceField(Organization))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
