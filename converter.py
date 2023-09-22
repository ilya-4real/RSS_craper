from json import dumps


def convert(xml_data: dict, json_path: str):
    json_data = dumps(xml_data)
    with open(json_path, 'w') as json_file:
        json_file.write(json_data)