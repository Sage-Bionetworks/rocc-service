import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.person import Person as DbPerson  # noqa: E501
from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_persons import PageOfPersons  # noqa: E501
from openapi_server.models.person import Person  # noqa: E501
from openapi_server.config import Config


def create_person(person=None):  # noqa: E501
    """Create a person

    Create a person with the specified name # noqa: E501

    :param person:
    :type person: dict | bytes

    :rtype: Person
    """
    res = None
    status = None
    try:
        if connexion.request.is_json:
            person = Person.from_dict(connexion.request.get_json())
            # Check that the organizations specified exist
            for org_id in person.organizations:
                try:
                    DbOrganization.objects.get(organizationId=org_id)
                except DoesNotExist:
                    status = 404
                    res = Error(
                        f'The organization {org_id} was not found',
                        status)
            # create the person
            if status is None:
                try:
                    db_person = DbPerson(
                        firstName=person.first_name,
                        lastName=person.last_name,
                        email=person.email,
                        organizations=person.organizations
                    ).save(force_insert=True)
                    res = Person.from_dict(db_person.to_dict())
                    status = 200
                except NotUniqueError as error:
                    status = 409
                    res = Error("Conflict", status, str(error))
        else:
            status = 400
            res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def delete_person(person_id):  # noqa: E501
    """Delete a person

    Deletes the person specified # noqa: E501

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    res = None
    status = None
    try:
        db_person = DbPerson.objects(personId=person_id).first()
        res = Person.from_dict(db_person.to_dict())
        db_person.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_person(person_id):  # noqa: E501
    """Get a person

    Returns the person specified # noqa: E501

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    res = None
    status = None
    try:
        db_person = DbPerson.objects(personId=person_id).first()
        res = Person.from_dict(db_person.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_persons(limit=None, offset=None):  # noqa: E501
    """Get all persons

    Returns the persons # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfPersons
    """
    res = None
    status = None
    try:
        db_persons = DbPerson.objects.skip(offset).limit(limit)
        persons = [Person.from_dict(d.to_dict()) for d in db_persons]
        next_ = ""
        if len(persons) == limit:
            next_ = "%s/persons?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfPersons(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            persons=persons)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
