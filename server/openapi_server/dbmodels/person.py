from mongoengine import Document, StringField, EmailField, ListField  # noqa: E501


class Person(Document):
    firstName = StringField(min_length=1)
    lastName = StringField(min_length=1)
    email = EmailField()
    organizations = ListField(StringField())

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["personId"] = str(self.pk)
        return doc
