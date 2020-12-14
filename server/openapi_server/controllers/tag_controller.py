import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.tag import Tag as DbTag  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_tags import PageOfTags  # noqa: E501
from openapi_server.models.tag import Tag  # noqa: E501
from openapi_server.config import Config


def create_tag(tag_id, tag=None):  # noqa: E501
    """Create a tag

    Create a tag with the specified name # noqa: E501

    :param tag_id: The ID of the tag that is being created
    :type tag_id: str
    :param tag:
    :type tag: dict | bytes

    :rtype: Tag
    """
    res = None
    status = None
    if tag_id is not None and connexion.request.is_json:
        try:
            tag = Tag.from_dict(connexion.request.get_json())
            tag.tag_id = tag_id
            db_tag = DbTag(
                tagId=tag.tag_id,
                description=tag.description
            ).save()
            res = Tag.from_dict(db_tag.to_dict())
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    else:
        status = 422
        res = Error("The query parameter datasetId is not specified", status)

    return res, status


def delete_tag(tag_id):  # noqa: E501
    """Delete a tag

    Deletes the tag specified # noqa: E501

    :param tag_id: The ID of the tag
    :type tag_id: str

    :rtype: Tag
    """
    res = None
    status = None
    try:
        db_tag = DbTag.objects.get(tagId=tag_id)
        res = Tag.from_dict(db_tag.to_dict())
        db_tag.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def get_tag(tag_id):  # noqa: E501
    """Get a tag

    Returns the tag specified # noqa: E501

    :param tag_id: The ID of the tag
    :type tag_id: str

    :rtype: Tag
    """
    res = None
    status = None
    try:
        db_tag = DbTag.objects.get(tagId=tag_id)
        res = Tag.from_dict(db_tag.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status


def list_tags(limit=None, offset=None):  # noqa: E501
    """Get all tags

    Returns the tags # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfTags
    """
    res = None
    status = None
    try:
        db_tags = DbTag.objects.skip(offset).limit(limit)
        tags = [Tag.from_dict(d.to_dict()) for d in db_tags]
        next_ = ""
        if len(tags) == limit:
            next_ = "%s/tags?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfTags(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            tags=tags)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
