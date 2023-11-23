from .abstract_writer import AbstractJsonWriter, AbstractTxtWriter, AbstractFormatChooser
from json import dumps

class WRiteFormatChooser(AbstractJsonWriter, AbstractTxtWriter):
    def __init__(self, json: bool) -> None:
        self.json = json

    def write(self, data: dict):
        if self.json:
            converted_data = self.convert_to_json(data)
            # print(converted_data)
            # print()
            # print(len(converted_data))
            # print()
            self.write_json(converted_data)
        else:
            self.write_txt(data)
    
    @staticmethod
    def convert_to_json(scraped_data: dict):
        return dumps(scraped_data, indent=2)


class Cli_writer(WRiteFormatChooser, AbstractJsonWriter, AbstractTxtWriter):

    def write_txt(self, data: dict) -> None:
        for key, value in data.items():
            if type(value) == list:
                for i in value:
                    self.write_txt(i)
            else:
                print(f'{key} : {value}\n')

    def write_json(self, data) -> None:
            print(data)


class File_Writer(WRiteFormatChooser, AbstractJsonWriter, AbstractTxtWriter):
    def __init__(self, filename: str, json: bool = False) -> None:
        super().__init__(json)
        if json:
            self.filename = filename + ".json"
        else:
            self.filename = filename + ".txt"
        self.json = json

    #FIXME problem with writing dictionary to the file
    
    def write_txt(self, data: dict, write_mod: str = 'w') -> None:
        with open(self.filename, write_mod) as file:
            for key, value in data.items():
                if type(value) == list:
                    for i in value:
                        self.write_txt(i, 'a')
                else:
                    file.write(f'{key} : {value}\n')

    def write_json(self, data):
        with open(self.filename, 'w') as file:
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
