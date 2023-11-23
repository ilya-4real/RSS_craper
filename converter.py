from json import dumps
from typing import Union


def convert_xml_to_json(xml_data: Union[list, dict]):
    json_data = dumps(xml_data, indent=2)
    return json_data