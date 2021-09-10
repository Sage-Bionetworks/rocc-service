import datetime
from mongoengine import DateTimeField, EmailField, StringField, URLField  # noqa: E501

from openapi_server.dbmodels.account import Account


class User(Account):
    email = EmailField()
    name = StringField()
    avatar_url = URLField()
    created_at = DateTimeField(required=True, default=datetime.datetime.now)
    updated_at = DateTimeField(required=True, default=datetime.datetime.now)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
