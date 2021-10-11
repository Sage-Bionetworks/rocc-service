import datetime
from bson import ObjectId
from mongoengine import DateTimeField, Document, ObjectIdField, StringField, ListField, ReferenceField  # noqa: E501

from openapi_server.dbmodels.challenge import Challenge


class ChallengeOrganizer(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True)
    login = StringField()
    organizerRoles = ListField(StringField(choices=["challenge_lead", "infrastructure_lead"]), default=[])  # noqa: E501
    challengeId = ReferenceField(Challenge, required=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        doc.pop('challengeId', None)
        return doc
