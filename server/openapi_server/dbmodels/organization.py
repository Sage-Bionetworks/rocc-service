import datetime
from mongoengine import DateTimeField, EmailField, StringField, URLField  # noqa: E501

from openapi_server.dbmodels.account import Account


class Organization(Account):
    email = EmailField()
    name = StringField()
    avatarUrl = URLField()
    description = StringField()
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
