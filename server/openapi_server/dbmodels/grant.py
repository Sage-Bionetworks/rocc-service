from mongoengine import StringField, LongField, IntField, URLField

from openapi_server.dbmodels.organization import Organization


class Grant(Document):
    name = StringField(required=True)
    description = LongField()
    sponsor = ReferenceField(Organization)
    amount = IntField()
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
