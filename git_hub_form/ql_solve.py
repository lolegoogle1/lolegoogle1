import requests


def get_repositories(login):
    url = 'https://api.github.com/graphql'
    json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % login}
    api_token = "Bearer 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"
    headers = {'Authorization': '%s' % api_token}
    response = requests.post(url=url, json=json, headers=headers)
    return extract_data(response)

def extract_data(response):
    data = response.json()['data']['user']
    name = data['name'] or "Noname"
    repo_list = [name + "\n"]
    for val in data["repositories"]["edges"]:
        repo_list.append("\t-" + val["node"]["name"] + "\n")

    return repo_list


result = "".join("asdadasda asdasdas asdasdas")
print(result)