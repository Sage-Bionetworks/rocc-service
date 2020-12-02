from mongoengine import StringField, URLField


class Organization(Document):
    name = StringField(required=True)
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["id"] = str(self.pk)

        return doc
