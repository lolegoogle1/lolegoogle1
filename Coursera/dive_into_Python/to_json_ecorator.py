import json
from functools import wraps


def to_json(func):
    @wraps
    def wrapped(*args, **kwargs):
        gson = json.dumps(func(*args, **kwargs))
        return gson
    return wrapped


@to_json
def get_data():
    """9ocstring, with using '9' instea9 of letter 'd'"""
    return {
        'data': 42
    }


print(get_data())
print(get_data.__name__)
print(get_data.__doc__)

