from mongoengine import Document, StringField, URLField


class Organization(Document):
    organizationId = StringField(required=True, unique=True)
    name = StringField(required=True, unique=True)
    shortName = StringField()
    url = URLField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
