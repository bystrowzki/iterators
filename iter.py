import requests
import json


class Countries:

    def __init__(self, path):
        self.file = open(path)

    def __iter__(self):
        self.country = json.load(self.file)
        return self

    def __next__(self):
        if not self.country:
            self.file.close()
            raise StopIteration
        country_name = self.country.pop()['name']['common']
        return country_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Countries('countries.json') as country_iter:
    for name in country_iter:
        print(name)
