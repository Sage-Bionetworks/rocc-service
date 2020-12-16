import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.dbmodels.challenge import Challenge as DbChallenge
from openapi_server.dbmodels.tag import Tag as DbTag
from openapi_server.models.challenge import Challenge
from openapi_server.models.error import Error
from openapi_server.models.page_of_challenges import PageOfChallenges
from openapi_server.config import Config


def create_challenge(challenge=None):
    """Add a challenge

    Adds a challenge

    :param challenge:
    :type challenge: dict | bytes

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        if connexion.request.is_json:
            challenge = Challenge.from_dict(connexion.request.get_json())
            for tag_id in challenge.tags:
                try:
                    DbTag.objects.get(tagId=tag_id)
                except DoesNotExist:
                    status = 404
                    res = Error(f"The tag, {tag_id}, was not found", status)
            if status is None:
                try:
                    db_challenge = DbChallenge(
                        name=challenge.name,
                        startDate=challenge.start_date,
                        endDate=challenge.end_date,
                        url=challenge.url,
                        status=challenge.status,
                        # grant=challenge.grant,
                        # organizers=challenge.organizers,
                        tags=challenge.tags
                    ).save(force_insert=True)
                    res = Challenge.from_dict(db_challenge.to_dict())
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


def delete_challenge(challenge_id):
    """Delete a challenge

    Deletes the challenge specified

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        db_challenge = DbChallenge.objects(challengeId=challenge_id).first()
        res = Challenge.from_dict(db_challenge.to_dict())
        db_challenge.delete()
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def get_challenge(challenge_id):
    """Get a challenge

    Returns the challenge specified

    :param challenge_id: The ID of the challenge
    :type challenge_id: str

    :rtype: Challenge
    """
    res = None
    status = None
    try:
        db_challenge = DbChallenge.objects(challengeId=challenge_id).first()
        res = Challenge.from_dict(db_challenge.to_dict())
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def list_challenges(limit=None, offset=None):
    """List all the challenges

    Returns all the challenges

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfChallenges
    """
    res = None
    status = None
    try:
        db_challenges = DbChallenge.objects.skip(offset).limit(limit)
        challenges = [Challenge.from_dict(d.to_dict()) for d in db_challenges]
        next_ = ""
        if len(challenges) == limit:
            next_ = "%s/challenges?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)
        res = PageOfChallenges(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            challenges=challenges)
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
