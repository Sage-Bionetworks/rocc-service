import datetime
from mongoengine import DateTimeField, EmailField, StringField, URLField  # noqa: E501
from werkzeug.security import check_password_hash

from openapi_server.dbmodels.account import Account


class User(Account):
    email = EmailField()
    name = StringField()
    avatarUrl = URLField()
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)
    passwordHash = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        doc.pop('passwordHash', None)
        return doc

    def verify_password(self, password):
        return check_password_hash(self.passwordHash, password)
