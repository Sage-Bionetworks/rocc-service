from bson import ObjectId
from mongoengine import DateTimeField, Document, ReferenceField, StringField, ObjectIdField, URLField, ListField  # noqa: E501

from openapi_server.dbmodels.account import Account
from openapi_server.dbmodels.challenge_platform import ChallengePlatform


class Challenge(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True)
    displayName = StringField(min_length=3, max_length=60)
    description = StringField(required=True)
    fullName = StringField(required=True, unique=True)
    ownerId = ReferenceField(Account)
    websiteUrl = URLField()
    status = StringField(
        # required=True,
        choices=["active", "upcoming", "completed"]  # TODO: DRY
    )
    startDate = DateTimeField()
    endDate = DateTimeField()
    platformId = ReferenceField(ChallengePlatform)
    topics = ListField(StringField(unique=True), default=[])
    doi = StringField()

    # summary = StringField()
    # startDate = DateTimeField()
    # endDate = DateTimeField()
    # url = URLField(required=True)
    # status = StringField(
    #     required=True,
    #     choices=["active", "upcoming", "completed"]  # TODO: DRY
    # )
    # tagIds = ListField(ReferenceField(Tag))
    # organizerIds = ListField(ReferenceField(Person))
    # dataProviderIds = ListField(ReferenceField(Organization))
    # grantIds = ListField(ReferenceField(Grant))
    # platformId = ReferenceField(ChallengePlatform)
    # createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    # updatedAt = DateTimeField(required=True, default=datetime.datetime.now)

    meta = {'indexes': [
        {
            'fields': ['$name', '$description', '$topics'],
            'default_language': 'english',
            'weights': {'name': 10, 'description': 2, 'topics': 8}
        }
    ]}

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)
        return doc
