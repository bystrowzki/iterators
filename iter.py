import re
import requests
import json
import hashlib

host = 'https://en.wikipedia.org/wiki'


def gen(path):
    with open(path) as file:
        for line in file:
            hash_object = hashlib.md5(line.encode())
            yield print(hash_object.hexdigest())

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
        if ' ' in country_name:
            name = country_name.replace(' ', '_')
            link = host+'/'+name
        else:
            link = host+'/'+country_name
        res = country_name+' - '+link
        with open('Countries List.txt', 'a+', encoding='UTF-8') as file:
            file.write(str(res)+'\n')
        return country_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Countries('countries.json') as country_iter:
    for name in country_iter:
        pass
        for item in gen('Countries List.txt'):
            pass

