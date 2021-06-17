from bson import ObjectId
from mongoengine import Document, StringField, URLField, ObjectIdField  # , ReferenceField # noqa: E501

# from openapi_server.dbmodels.organization import Organization


class Grant(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True, unique=True)
    description = StringField()
    # sponsor = ReferenceField(Organization, required=True)
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        doc.pop('_id', None)
        return doc
