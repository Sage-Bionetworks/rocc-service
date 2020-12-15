import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.organization import Organization as DbOrganization  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.models.page_of_organizations import PageOfOrganizations  # noqa: E501
from openapi_server.config import Config


def create_organization(organization_id, organization=None):  # noqa: E501
    """Create an organization

    Create an organization with the specified name # noqa: E501

    :param organization_id: The ID of the organization that is being created
    :type organization_id: str
    :param organization:
    :type organization: dict | bytes

    :rtype: Organization
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            org = Organization.from_dict(connexion.request.get_json())
            org.organization_id = organization_id
            db_org = DbOrganization(
                organizationId=org.organization_id,
                name=org.name,
                shortName=org.short_name,
                url=org.url
            ).save(force_insert=True)
            res = Organization.from_dict(db_org.to_dict())
            status = 200
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


def delete_organization(organization_id):  # noqa: E501
    """Delete an organization

    Deletes the organization specified # noqa: E501

    :param organization_id: The ID of the organization
    :type organization_id: str

    :rtype: Organization
    """
    res = None
    status = None
    try:
        db_org = DbOrganization.objects.get(organizationId=organization_id)
        res = Organization.from_dict(db_org.to_dict())
        db_org.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_organization(organization_id):  # noqa: E501
    """Get an organization

    Returns the organization specified # noqa: E501

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


def list_organizations(limit=None, offset=None):  # noqa: E501
    """Get all organizations

    Returns the organizations # noqa: E501

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
            organizations=orgs)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
