import datetime
import os

import peewee
from playhouse.db_url import connect
from playhouse.postgres_ext import JSONField

DB = connect(
    os.environ.get('DATABASE_URL',
                   'postgres://postgres:postgres@localhost:5432/weather'))


# define a base model class that points at the database object you wish to use, and then all your models will extend it:
class BaseModel(peewee.Model):
    class Meta:
        database = DB


class Weather(BaseModel):
    city = peewee.CharField(max_length=60)
    weather_data = JSONField()
    created = peewee.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.city
