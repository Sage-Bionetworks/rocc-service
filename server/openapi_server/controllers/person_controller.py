import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_persons import PageOfPersons  # noqa: E501
from openapi_server.models.person import Person  # noqa: E501
from openapi_server import util


def create_person(person=None):  # noqa: E501
    """Create a person

    Create a person with the specified name # noqa: E501

    :param person: 
    :type person: dict | bytes

    :rtype: Person
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_person(person_id):  # noqa: E501
    """Delete a person

    Deletes the person specified # noqa: E501

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    return 'do some magic!'


def get_person(person_id):  # noqa: E501
    """Get a person

    Returns the person specified # noqa: E501

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    return 'do some magic!'


def list_persons(limit=None, offset=None):  # noqa: E501
    """Get all persons

    Returns the persons # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfPersons
    """
    return 'do some magic!'
