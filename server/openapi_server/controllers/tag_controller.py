import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
# from mongoengine.queryset.visitor import Q

from openapi_server.dbmodels.tag import Tag as DbTag
from openapi_server.models.error import Error
from openapi_server.models.page_of_tags import PageOfTags
from openapi_server.models.tag import Tag
from openapi_server.models.tag_create_response import TagCreateResponse
from openapi_server.config import Config


def create_tag(tag_id):
    """Create a tag

    Create a tag with the specified name

    :param tag_id: The ID of the tag that is being created
    :type tag_id: str

    :rtype: Tag
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            tag = Tag.from_dict(connexion.request.get_json())
            DbTag(
                id=tag_id,
                description=tag.description
            ).save(force_insert=True)
            res = TagCreateResponse(id=tag_id)
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


def delete_tag(tag_id):
    """Delete a tag

    Deletes the tag specified

    :param tag_id: The ID of the tag
    :type tag_id: str

    :rtype: Tag
    """
    res = None
    status = None
    try:
        DbTag.objects.get(id=tag_id).delete()
        res = {}
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_tag(tag_id):
    """Get a tag

    Returns the tag specified

    :param tag_id: The ID of the tag
    :type tag_id: str

    :rtype: Tag
    """
    res = None
    status = None
    try:
        db_tag = DbTag.objects.get(id=tag_id)
        res = Tag.from_dict(db_tag.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_tags(limit=None, offset=None):
    """Get all tags

    Returns the tags

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfTags
    """
    res = None
    status = None
    try:
        # Get results based on query, limit and offset.
        # tag_id_q = Q(id__istartswith=filter_['id']) \
        #     if 'id' in filter_ else Q()
        db_tags = DbTag.objects().skip(offset).limit(limit)
        tags = [Tag.from_dict(d.to_dict()) for d in db_tags]
        next_ = ""
        if len(tags) == limit:
            next_ = "%s/tags?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)

        # Get total results count.
        total = db_tags.count()

        res = PageOfTags(
            offset=offset,
            limit=limit,
            paging={
                "next": next_
            },
            total_results=total,
            tags=tags)
        status = 200
    except TypeError:  # TODO: may need different exception
        status = 400
        res = Error("Bad request", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_all_tags():
    """Delete all tags

    Delete all tags # noqa: E501

    :rtype: object
    """
    res = None
    status = None
    try:
        DbTag.objects.delete()
        res = {}
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
