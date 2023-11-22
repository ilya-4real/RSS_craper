from requests import get

class DataParser:
    def __init__(self, url) -> None:
        self.url = url

    def get_data(self):
        data = get(self.url)
        return data.text
