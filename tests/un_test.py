json = {'query': '{user(login: ""){name repositories(first: 100){edges{node{name}}}} }'}
sto = "{'query': '{user(login: ""){name repositories(first: 100){edges{node{name}}}} }'}"
data = {'data': {'user': None}, 'errors': [{'type': 'NOT_FOUND', 'path': ['user'], 'locations': [{'line': 1, 'column': 2}], 'message': "Could not resolve to a User with the login of '0.124124.457456723'."}]}
print(data["errors"][0]["type"])
