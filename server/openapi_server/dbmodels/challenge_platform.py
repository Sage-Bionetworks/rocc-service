from mongoengine import Document, StringField


class ChallengePlatform(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True, unique=True)
    url = URLField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)
    updatedAt = DateTimeField(required=True, default=datetime.datetime.now)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        doc.pop('_id', None)
        return doc
