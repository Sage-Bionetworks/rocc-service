import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.models.error import Error
from openapi_server.models.organization import Organization
from openapi_server.models.organization_create_response import OrganizationCreateResponse  # noqa: E501
from openapi_server.models.page_of_organizations import PageOfOrganizations  # noqa: E501
from openapi_server.config import Config


def create_organization(organization_id):
    """Create an organization

    Create an organization with the specified name

    :param organization_id: The ID of the organization that is being created
    :type organization_id: str

    :rtype: Organization
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            org = Organization.from_dict(connexion.request.get_json())
            DbOrganization(
                organizationId=organization_id,
                name=org.name,
                shortName=org.short_name,
                url=org.url
            ).save(force_insert=True)
            res = OrganizationCreateResponse(organization_id=organization_id)
            status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 400
        res = Error("Bad request", status)

    return res, status


def delete_organization(organization_id):
    """Delete an organization

    Deletes the organization specified

    :param organization_id: The ID of the organization
    :type organization_id: str

    :rtype: Organization
    """
    res = None
    status = None
    try:
        DbOrganization.objects.get(organizationId=organization_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_organization(organization_id):
    """Get an organization

    Returns the organization specified

    :param organization_id: The ID of the organization
    :type organization_id: str

    :rtype: Organization
    """
    res = None
    status = None
    try:
        db_org = DbOrganization.objects.get(organizationId=organization_id)
        res = Organization.from_dict(db_org.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_organizations(limit=None, offset=None):
    """Get all organizations

    Returns the organizations

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfOrganizations
    """
    res = None
    status = None
    try:
        db_orgs = DbOrganization.objects.skip(offset).limit(limit)
        orgs = [Organization.from_dict(d.to_dict()) for d in db_orgs]
        next_ = ""
        if len(orgs) == limit:
            next_ = "%s/orgs?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfOrganizations(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=len(orgs),
            organizations=orgs)
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
