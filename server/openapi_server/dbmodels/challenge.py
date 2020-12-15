from mongoengine import DateTimeField, ListField, ReferenceField, StringField, URLField  # noqa: E501

from openapi_server.dbmodels.base_document import BaseDocument
from openapi_server.dbmodels.grant import Grant
# from openapi_server.dbmodels.person import Person


class Challenge(BaseDocument):
    name = StringField(required=True, unique=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    url = URLField()
    status = StringField(
        required=True,
        choices=["open", "upcoming", "closed"]
    )
    tags = ListField(StringField(max_length=30))
    grant = ListField(ReferenceField(Grant))
    # organizers = ListField(ReferenceField(Person))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)
        return doc
