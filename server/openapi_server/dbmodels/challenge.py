from bson import ObjectId
from mongoengine import Document, DateTimeField, ListField, ReferenceField, StringField, URLField, ObjectIdField  # noqa: E501

from openapi_server.dbmodels.tag import Tag
# from openapi_server.dbmodels.grant import Grant
# from openapi_server.dbmodels.person import Person


class Challenge(Document):
    challengeId = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True, unique=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    url = URLField()
    status = StringField(
        required=True,
        choices=["open", "upcoming", "closed"]
    )
    # grant = ListField(ReferenceField(Grant))
    # organizers = ListField(ReferenceField(Person))
    tags = ListField(ReferenceField(Tag))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["challengeId"] = str(self.pk)
        return doc
