from bson import ObjectId
from mongoengine import Document, ObjectIdField, StringField


class Account(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    login = StringField(required=True, unique=True)
    type = StringField(
        required=True,
        choices=["User", "Organization"]
    )

    meta = {'allow_inheritance': True}

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
