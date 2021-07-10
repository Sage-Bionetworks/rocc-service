from bson import ObjectId
import datetime
from mongoengine import Document, DateTimeField, ListField, ReferenceField, StringField, URLField, ObjectIdField  # noqa: E501

# from openapi_server.dbmodels.challenge_results import ChallengeResults
from openapi_server.dbmodels.tag import Tag
from openapi_server.dbmodels.person import Person
from openapi_server.dbmodels.organization import Organization
from openapi_server.dbmodels.grant import Grant


class Challenge(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True, unique=True)
    description = StringField(required=True)
    summary = StringField()
    startDate = DateTimeField()
    endDate = DateTimeField()
    url = URLField(required=True)
    status = StringField(
        required=True,
        choices=["open", "upcoming", "closed"]
    )
    tagIds = ListField(ReferenceField(Tag))
    organizerIds = ListField(ReferenceField(Person))
    dataProviderIds = ListField(ReferenceField(Organization))
    grantIds = ListField(ReferenceField(Grant))
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)
    # challengeResults = EmbeddedDocumentField(ChallengeResults)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        doc.pop('_id', None)
        return doc
