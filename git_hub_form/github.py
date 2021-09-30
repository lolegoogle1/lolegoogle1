import requests
import json
from unittest import TestCase
from urllib3.exceptions import MaxRetryError, NewConnectionError
import functools

login = ['crankerkor', 'lolegoogle1', 'LunaLovegoood', 'Yurii-Khomiak', 'dhmfu', 'aasdasdas', 1232, 0.1231, '^&#61927']


class BadCredentialsException(Exception):
    pass


def raise_exception(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            print(data.status_code)
            if data.status_code == 401:
                raise BadCredentialsException
            elif data.status_code == 400:
                raise requests.exceptions.ConnectionError
            elif data["errors"][0]["type"] == 'NOT_FOUND':
                raise TypeError
        except TypeError:
            return 'There is no such user: ', ""
        except requests.exceptions.ConnectionError:
            return "I'm sorry. The connection can't be established at the moment", ""
        except BadCredentialsException:
            return "Sorry for inconvenience. Please contact with the host to solve the problem", ""

        return data.json()
    return wrapped


@raise_exception
def github_api(error_type):
    json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % "lolegoogle1"}
    api_token = "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"
    if 'TypeError' in error_type:
        json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % "0.124124.457456723"}
    elif 'ConnectionError' in error_type:
        json = str(json)
    elif 'BadCredentialsException' in error_type:
        api_token = "asd1234124215421asd124"
    response = requests.post(
        url='https://api.github.com/graphql',
        json=json,
        headers={'Authorization': 'Bearer %s' % api_token}
    )
    return response

print(github_api("TypeError"))

def get_repositories(login):
    url = 'https://api.github.com/graphql'
    json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % login}
    api_token = "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"
    headers = {'Authorization': 'Bearer %s' % api_token}
    try:
        response = requests.post(url=url, json=json, headers=headers)
        return response.json()

        #return extract_data(response)
    except TypeError:
        return 'There is no such user, there are only: ', "TypeError Exception"
    except requests.exceptions.ConnectionError:
        return "I'm sorry. The connection can't be established at the moment", ""



def extract_data(response):
    data = response.json()['data']['user']
    name = data['name'] or "Noname\n"
    name = name+"\n"
    repo_list = []
    for val in data["repositories"]["edges"]:
        repo_list.append("\t-" + val["node"]["name"] + "\n")
    return name, repo_list

print(get_repositories("lolegoogle1"))