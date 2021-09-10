from mongoengine import Document, ReferenceField, StringField  # noqa: E501

from openapi_server.dbmodels.organization import Organization
from openapi_server.dbmodels.user import User


class OrgMembership(Document):
    state = StringField(
        required=True,
        choices=["active", "pending"]  # TODO: DRY
    )
    role = StringField(
        required=True,
        choices=["admin", "member"]  # TODO: DRY
    )
    organization_id = ReferenceField(Organization)
    user_id = ReferenceField(User, unique_with='organization_id')

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        doc['id'] = str(self.pk)
        return doc
