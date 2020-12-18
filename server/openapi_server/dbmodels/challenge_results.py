from mongoengine import EmbeddedDocument, IntField


class ChallengeResults(EmbeddedDocument):
    nSubmissions = IntField()
    nFinalSubmissions = IntField()
    nRegisteredParticipants = IntField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
