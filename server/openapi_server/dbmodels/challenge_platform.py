import datetime
from bson import ObjectId
from mongoengine import DateTimeField, Document, ObjectIdField, StringField, URLField  # noqa: E501


class ChallengePlatform(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(required=True, unique=True)
    display_name = StringField(required=True, unique=True)
    website_url = URLField(required=True)
    avatar_url = URLField()
    created_at = DateTimeField(required=True, default=datetime.datetime.now)
    updated_at = DateTimeField(required=True, default=datetime.datetime.now)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
