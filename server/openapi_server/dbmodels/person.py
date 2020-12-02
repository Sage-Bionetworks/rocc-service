from mongoengine import StringField, EmailField


class Person(Document):
    name = StringField(required=True)
    firstName = StringField()
    lastName = StringField()
    email = EmailField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
