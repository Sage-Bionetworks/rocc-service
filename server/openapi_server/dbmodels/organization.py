from mongoengine import Document, StringField, URLField


class Organization(Document):
    organizationId = StringField(primary_key=True)
    name = StringField(required=True, unique=True)
    shortName = StringField()
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc["organizationId"] = str(self.pk)
        doc.pop('_id', None)
        return doc
