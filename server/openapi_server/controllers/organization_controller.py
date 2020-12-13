import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.models.page_of_organizations import PageOfOrganizations  # noqa: E501
from openapi_server import util


def create_organization(organization_id, organization=None):  # noqa: E501
    """Create an organization

    Create an organization with the specified name # noqa: E501

    :param organization_id: The ID of the organization that is being created
    :type organization_id: str
    :param organization: 
    :type organization: dict | bytes

    :rtype: Organization
    """
    if connexion.request.is_json:
        organization = Organization.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_organization(organization_id):  # noqa: E501
    """Delete an organization

    Deletes the organization specified # noqa: E501

    :param organization_id: The ID of the organization
    :type organization_id: str

    :rtype: Organization
    """
    return 'do some magic!'


def get_organization(organization_id):  # noqa: E501
    """Get an organization

    Returns the organization specified # noqa: E501

    :param organization_id: The ID of the organization
    :type organization_id: str

    :rtype: Organization
    """
    return 'do some magic!'


def list_organizations(limit=None, offset=None):  # noqa: E501
    """Get all organizations

    Returns the organizations # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfOrganizations
    """
    return 'do some magic!'
