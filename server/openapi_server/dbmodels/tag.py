from mongoengine import Document, StringField


class Tag(Document):
    id = StringField(primary_key=True)
    description = StringField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        doc.pop('_id', None)
        return doc
