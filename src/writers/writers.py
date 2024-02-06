from ..tools.json_converter import convert_to_json
from ..tools.filename_gen import filename_gen_fun
from ..tools.logger import init_logger
from ..config import PATH_TO_DATA_FOLDER
from .abstract_writers import (
    AbstractJsonWriter,
    AbstractTxtWriter,
    AbstractFormatChooser,
)


logger = init_logger("data writer", 20)


class FormatChooser(AbstractTxtWriter, AbstractJsonWriter, AbstractFormatChooser):

    def __init__(self, json: bool = False) -> None:
        super().__init__()
        self.json = json

    def write(self, data) -> None:
        if self.json:
            self.write_json(convert_to_json(data))  # type: ignore
        else:
            self.write_txt(data)


class CliWriter(FormatChooser):
    def write_txt(self, data: dict[str, str | list]) -> None:
        for key, value in data.items():
            if isinstance(value, list):
                for i in value:
                    self.write_txt(i)
            else:
                print(f"{key} : {value}\n")

    @staticmethod
    def write_json(data) -> None:
        print(data)


class FileWriter(FormatChooser):
    def __init__(self, json: bool = False, write_mod: str = "w") -> None:
        self.filename_gen = filename_gen_fun(json)
        self.filename = next(self.filename_gen)
        self.write_mod = write_mod
        super().__init__(json)

    def write_txt(self, data: dict[str, str | list]) -> None:
        logger.info(f"writing text to {self.filename}")
        with open(PATH_TO_DATA_FOLDER + self.filename, self.write_mod) as file:
            for key, value in data.items():
                if isinstance(value, list):
                    for i in value:
                        for key, value in i.items():
                            file.write(f"{key} : {value}\n")
                else:
                    file.write(f"{key} : {value}\n")

    def write_json(self, data: str):
        with open(PATH_TO_DATA_FOLDER + self.filename, self.write_mod) as file:
            logger.info(f"writing JSON to {self.filename}")
            file.write(data)
