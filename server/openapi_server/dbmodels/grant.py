from mongoengine import Document, ReferenceField, StringField, LongField, IntField, URLField  # noqa: E501

from openapi_server.dbmodels.organization import Organization


class Grant(Document):
    name = StringField(required=True)
    description = LongField()
    sponsor = ReferenceField(Organization, required=True)
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        return doc
