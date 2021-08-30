import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_tags import PageOfTags  # noqa: E501
from openapi_server.models.tag import Tag  # noqa: E501
from openapi_server.models.tag_create_request import TagCreateRequest  # noqa: E501
from openapi_server.models.tag_create_response import TagCreateResponse  # noqa: E501
from openapi_server import util


def create_tag(tag_create_request):  # noqa: E501
    """Create a tag

    Create a tag with the specified name # noqa: E501

    :param tag_create_request: 
    :type tag_create_request: dict | bytes

    :rtype: TagCreateResponse
    """
    if connexion.request.is_json:
        tag_create_request = TagCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_all_tags():  # noqa: E501
    """Delete all tags

    Delete all tags # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def delete_tag(tag_id):  # noqa: E501
    """Delete a tag

    Deletes the tag specified # noqa: E501

    :param tag_id: The unique identifier of the tag
    :type tag_id: str

    :rtype: object
    """
    return 'do some magic!'


def get_tag(tag_id):  # noqa: E501
    """Get a tag

    Returns the tag specified # noqa: E501

    :param tag_id: The unique identifier of the tag
    :type tag_id: str

    :rtype: Tag
    """
    return 'do some magic!'


def list_tags(limit=None, offset=None):  # noqa: E501
    """Get all tags

    Returns the tags # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfTags
    """
    return 'do some magic!'
