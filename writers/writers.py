from .abstract_writer import AbstractJsonWriter, AbstractTxtWriter


class Cli_writer(AbstractTxtWriter, AbstractJsonWriter):
    def __init__(self, json: bool = False) -> None:
        self.json = json

    def write_txt(self, *data) -> None:
        for key, value in data[0].items():
            print(f'{key} : {value}')

        for i in data[1]:
            for key, value in i.items():
                if key == 'link':
                    print()
                print(f'{key} : {value}')
            print()

    @staticmethod
    def write_json(*data) -> None:
        for i in data:
            print(i)

    def write(self, *data):
        if self.json:
            self.write_json(*data)
        else:
            self.write_txt(*data)


class File_Writer(AbstractJsonWriter, AbstractTxtWriter):
    def __init__(self, filename: str, json: bool = False) -> None:
        super().__init__()
        if json:
            self.filename = filename + ".json"
        else:
            self.filename = filename + ".txt"
        self.json = json

    def write_txt(self, *data, write_mod: str = 'w') -> None:
        with open(self.filename, write_mod) as file:
            for key, value in data[0].items():
                file.write(f'{key} : {value}\n')
            file.write('\n')

            for i in data[1]:
                for key, value in i.items():
                    if key == 'link':
                        file.write("\n")
                    file.write(f'{key} : {value}\n')
                file.write("\n")

    def write_json(self, *data):
        with open(self.filename, 'w') as file:
            for i in data:
                file.write(i)

    def write(self, *data):
        if self.json:
            self.write_json(*data)
        else:
            self.write_txt(*data)


class Writer:
    def __init__(self, filename: str = None, json: bool = False) -> None:
        if not filename:
            self.writer = Cli_writer(json)
        else:
            self.filename = filename
            self.writer = File_Writer(filename, json)

    def write(self, *data):
        self.writer.write(*data)


