from mongoengine import EmbeddedDocument, IntField


class ChallengeResults(EmbeddedDocument):
    nFinalSubmissions = IntField()
    nRegisteredParticipants = IntField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc.pop('_id', None)
        return doc
