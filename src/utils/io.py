import json as js
from types import SimpleNamespace

def read_json(json_file):

    with open(json_file) as f:
        data = js.load(f)
        data = SimpleNamespace(**data)
        return data
