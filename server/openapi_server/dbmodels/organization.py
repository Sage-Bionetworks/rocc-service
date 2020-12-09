from mongoengine import Document, StringField, URLField  # noqa: E501


class Organization(Document):
    name = StringField(required=True)
    url = URLField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)
        return doc
