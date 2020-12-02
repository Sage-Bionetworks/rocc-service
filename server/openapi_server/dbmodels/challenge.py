from mongoengine import StringField, URLField, DateTimeField

from openapi_server.dbmodels.grant import Grant
from openapi_server.dbmodels.person import Person


class Challenge(Document):
    name = StringField(required=True)
    startDate = DateTimeField()
    endDate = DateTimeField()
    url = URLField()
    status = StringField()
    tags = ListField(StringField(max_length=30))
    grant = ListField(ReferenceField(Grant))
    organizers = ListField(ReferenceField(Person))

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
