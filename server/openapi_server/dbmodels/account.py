import datetime
from mongoengine import DateTimeField, Document, EmailField, ObjectIdField, StringField, URLField  # noqa: E501


class Account(Document):
    id = ObjectIdField()
    login = StringField(required=True)
    email = EmailField()
    name = StringField()
    avatarUrl = URLField()
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)
    type = StringField(
        required=True,
        choices=["User", "Organization"]
    )

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        doc.pop('_id', None)
        return doc
