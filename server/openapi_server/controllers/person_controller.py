import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
from mongoengine.queryset.visitor import Q

from openapi_server.dbmodels.person import Person as DbPerson
from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.models.error import Error
from openapi_server.models.page_of_persons import PageOfPersons
from openapi_server.models.person import Person
from openapi_server.models.person_create_response import PersonCreateResponse
from openapi_server.config import Config


def create_person():
    """Create a person

    Create a person with the specified name

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
                        f"The organization {org_id} was not found",
                        status)
                    return res, status

            # Create the person
            try:
                db_person = DbPerson(
                    firstName=person.first_name,
                    lastName=person.last_name,
                    email=person.email,
                    organizations=person.organizations
                ).save(force_insert=True)
                new_id = db_person.to_dict().get("personId")
                res = PersonCreateResponse(person_id=new_id)
                status = 201
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


def delete_person(person_id):
    """Delete a person

    Deletes the person specified

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    res = None
    status = None
    try:
        DbPerson.objects.get(personId=person_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_person(person_id):
    """Get a person

    Returns the person specified

    :param person_id: The ID of the person
    :type person_id: str

    :rtype: Person
    """
    res = None
    status = None
    try:
        db_person = DbPerson.objects.get(personId=person_id)
        res = Person.from_dict(db_person.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_persons(limit=None, offset=None, filter_=None):
    """Get all persons

    Returns the persons

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfPersons
    """
    res = None
    status = None
    try:
        # Get results based on query, limit and offset.
        first_name_q = Q(firstName__istartswith=filter_['firstName']) \
            if 'firstName' in filter_ else Q()
        last_name_q = Q(lastName__istartswith=filter_['lastName']) \
            if 'lastName' in filter_ else Q()
        email_q = Q(email=filter_['email']) \
            if 'email' in filter_ else Q()
        organization_q = Q(organizations__contains=filter_['organization']) \
            if 'organization' in filter_ else Q()
        db_persons = DbPerson.objects(
            first_name_q & last_name_q & email_q & organization_q
        ).skip(offset).limit(limit)
        persons = [Person.from_dict(d.to_dict()) for d in db_persons]
        next_ = ""
        if len(persons) == limit:
            next_ = "%s/persons?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)

        # Get total results count.
        total = DbPerson.objects.count()

        res = PageOfPersons(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=total,
            persons=persons)
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def delete_all_persons():
    """Delete all persons

    Delete all persons # noqa: E501

    :rtype: object
    """
    res = None
    status = None
    try:
        DbPerson.objects.delete()
        res = {}
        status = 200
    # TODO: find an exception that will raise 400 error
    # except DoesNotExist:
    #     status = 400
    #     res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
