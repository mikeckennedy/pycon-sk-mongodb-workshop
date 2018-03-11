import datetime

import mongoengine


class TestThing(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField()
    size = mongoengine.IntField()


class TestDownload(mongoengine.Document):
    create = mongoengine.DateTimeField(default=datetime.datetime.now)
    client = mongoengine.StringField()
    version = mongoengine.StringField(required=True)
    things = mongoengine.EmbeddedDocumentListField(TestThing)

    meta = {
        'db_alias': 'core',
        'collection': 'test_downloads',
        'indexes': [
            'version',
            'things.size'
        ]
    }
