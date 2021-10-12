import datetime
from bson import ObjectId
from mongoengine import DateTimeField, Document, ObjectIdField, StringField, ReferenceField, IntField  # noqa: E501

from openapi_server.dbmodels.challenge import Challenge


class ChallengeReadme(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    text = StringField(required=True)
    challengeId = ReferenceField(Challenge, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)
    v = IntField(db_field='__v')

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
