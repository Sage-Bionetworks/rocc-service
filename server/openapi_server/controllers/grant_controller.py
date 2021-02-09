import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.grant import Grant as DbGrant
from openapi_server.models.error import Error
from openapi_server.models.grant import Grant
from openapi_server.models.grant_create_response import GrantCreateResponse
from openapi_server.models.page_of_grants import PageOfGrants
from openapi_server.config import Config


def create_grant():
    """Create a grant

    Create a grant with the specified name

    :rtype: Grant
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            grant = Grant.from_dict(connexion.request.get_json())
            db_grant = DbGrant(
                name=grant.name,
                description=grant.description,
                # sponsor=grant.sponsor,
                url=grant.url
            ).save(force_insert=True)
            new_id = db_grant.to_dict().get("grantId")
            res = GrantCreateResponse(grant_id=new_id)
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


def delete_grant(grant_id):
    """Delete a grant

    Deletes the grant specified

    :param grant_id: The ID of the grant that is being created
    :type grant_id: str

    :rtype: Grant
    """
    res = None
    status = None
    try:
        DbGrant.objects.get(grantId=grant_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_grant(grant_id):
    """Get a grant

    Returns the grant specified

    :param grant_id: The ID of the grant that is being created
    :type grant_id: str

    :rtype: Grant
    """
    res = None
    status = None
    try:
        db_grant = DbGrant.objects.get(grantId=grant_id)
        res = Grant.from_dict(db_grant.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_grants(limit=None, offset=None):
    """Get all grants

    Returns the grants

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfGrants
    """
    res = None
    status = None
    try:
        # Get results based on limit and offset.
        db_grants = DbGrant.objects.skip(offset).limit(limit)
        grants = [Grant.from_dict(d.to_dict()) for d in db_grants]
        next_ = ""
        if len(grants) == limit:
            next_ = "%s/grants?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)

        # Get total results count.
        total = DbGrant.objects.count()

        res = PageOfGrants(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            total_results=total,
            grants=grants)
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_all_grants():
    """Delete all grants

    Delete all grants # noqa: E501

    :rtype: object
    """
    res = None
    status = None
    try:
        DbGrant.objects.delete()
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
