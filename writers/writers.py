from .abstract_writers import AbstractJsonWriter, AbstractTxtWriter, AbstractFormatChooser
from json import dumps
from tools.logger import init_logger

logger = init_logger("data writer", 20)

PATH_TO_DATA_FOLDER = "data/"

class FormatChooser(AbstractFormatChooser):
    
    def __init__(self, json: bool = False) -> None:
        super().__init__()
        self.json = json

    def write(self, data):
        if self.json:
            self.write_json(self.convert_to_json(data))
        else:
            self.write_txt(data)

    @staticmethod
    def convert_to_json(data):
        logger.info("converting to JSON")
        return dumps(data, indent=2)


class Cli_writer(AbstractTxtWriter, AbstractJsonWriter, FormatChooser):
    def write_txt(self, data: dict) -> None:
        for key, value in data.items():
            if type(value) == list:
                for i in value:
                    self.write_txt(i)
            else:
                print(f'{key} : {value}\n')
        
    @staticmethod
    def write_json(data) -> None:
            print(data)


class File_Writer(AbstractJsonWriter, AbstractTxtWriter, FormatChooser):
    def __init__(self, filename: str, json: bool = False) -> None:
        if json:
            self.filename = filename + ".json"
        else:
            self.filename = filename + ".txt"
        super().__init__(json)

    def write_txt(self, data, write_mod: str = 'w') -> None:
        logger.info("writing text to the file")
        with open(PATH_TO_DATA_FOLDER + self.filename, write_mod) as file:
            for key, value in data.items():
                if type(value) == list:
                    for i in value:
                        for key, value in i.items():
                            file.write(f'{key} : {value}\n')
                else:
                    file.write(f'{key} : {value}\n')

    def write_json(self, data):
        with open(PATH_TO_DATA_FOLDER + self.filename, 'w') as file:
                logger.info("writing JSON to the file")
                file.write(data)


class Writer:
    def __init__(self, filename: str = None, json: bool = False) -> None:
        if not filename:
            self.writer = Cli_writer(json)
        else:
            self.filename = filename
            self.writer = File_Writer(filename, json)

    def write(self, data):
        self.writer.write(data)


