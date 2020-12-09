from mongoengine import Document, StringField, EmailField  # noqa: E501


class Person(Document):
    firstName = StringField(required=True, min_length=1)
    lastName = StringField(min_length=1)
    email = EmailField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)
        return doc
