from mongoengine import Document, StringField


class Tag(Document):
    tagId = StringField(primary_key=True)
    description = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['tagId'] = str(self.pk)
        doc.pop('_id', None)
        return doc
