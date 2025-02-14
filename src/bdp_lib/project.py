from jsonschema import validate
from .schema import schema


class Project:
    def __init__(self, json: dict):
        self.raw_data = json


def load_project(json: dict):
    validate(json, schema)
    return Project(json)
