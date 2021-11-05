import datetime
from bson import ObjectId
from mongoengine import DateTimeField, Document, ObjectIdField, StringField, IntField  # noqa: E501


class Registry(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True)
    description = StringField(required=True)
    userCount = IntField(required=True)
    orgCount = IntField(required=True)
    challengeCount = IntField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)
    v = IntField(db_field='__v')

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
