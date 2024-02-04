from json import dumps


def convert_to_json(data: dict):
    return dumps(data, indent=2)
