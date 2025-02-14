class Project:
    def __init__(self, json: dict):
        self.raw_data = json


def validate_schema(json: dict) -> bool:
    return True


def load_project(json: dict):
    assert validate_schema(json)
    return Project(json)
