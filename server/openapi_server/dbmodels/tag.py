from mongoengine import Document, StringField


class Tag(Document):
    tagId = StringField(required=True, unique=True)
    description = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
