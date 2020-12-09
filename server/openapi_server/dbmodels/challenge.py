from mongoengine import Document, ListField, ReferenceField, StringField, URLField  # noqa: E501

from openapi_server.dbmodels.grant import Grant
from openapi_server.dbmodels.person import Person


class Challenge(Document):
    name = StringField(required=True, unique=True)
    startDate = StringField(required=True, regex=r"^\d{4}(-\d{2})?(-\d{2})?$")
    endDate = StringField(required=True, regex=r"^\d{4}(-\d{2})?(-\d{2})?$")
    url = URLField()
    status = StringField(
        required=True,
        choices=["open", "upcoming", "closed"]
    )
    tags = ListField(StringField(max_length=30))
    grant = ListField(ReferenceField(Grant))
    organizers = ListField(ReferenceField(Person))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)
        return doc
