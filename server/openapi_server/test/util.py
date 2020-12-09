from mongoengine import connect, disconnect

from openapi_server.dbmodels.challenge import Challenge


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_challenge(challenge_id):
    return Challenge(
        name='challenges/{challenge_id}'.format(challenge_id=challenge_id),
        startDate="2020",
        endDate="2020",
        status="open"
    ).save()
