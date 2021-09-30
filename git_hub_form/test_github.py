import unittest

from github import *

# ============== Test Data for Users ==================
test_data = {
    "crankerkor": ('Oleksandr Lutsenko\n',
                   ['\t-nodejs-examples\n', '\t-crankerkor.github.io\n',
                    '\t-lil-trip\n', '\t-PowershapeLab1\n',
                    '\t-discrete-model-labs\n', '\t-da\n'
                    ]
                   ),

    "lolegoogle1": ('Oleh Hryshcuk\n',
                    ['\t-lolegoogle1\n', '\t-DjangoProjects\n']),

    "LunaLovegoood": ('Loony\n',
                      ['\t-matrix\n', '\t-random-walker\n',
                       '\t-langtons-ant\n', '\t-barnsley-fern\n',
                       '\t-PI-monte-carlo\n', '\t-n-puzzle\n',
                       '\t-PowershapeLab1\n', '\t-simple-game-engine\n',
                       '\t-traffic-flow\n', '\t-matrix-digital-rain\n',
                       '\t-parallel-computing\n', '\t-ahk-scripts\n',
                       '\t-discrete-models-labs\n'
                       ]
                      ),

    "Yurii-Khomiak": ('Yurii Khomiak\n',
                      ['\t-dotfiles\n', '\t-yt-audio-playlist-downloader\n',
                       '\t-nvim-config\n'
                       ]
                      ),

    "dhmfu": ('Vasil Dudka\n',
              ['\t-umka-carboncalc\n', '\t-checklist-app\n',
               '\t-checklist-app-server\n'
               ]
              ),

    "aasdasdas": ('Noname\n\n', []),

    "1232": ('Noname\n\n', ['\t-amine\n']),

    "0.1231": ('There is no such user, there are only: ',
               'TypeError Exception'
               ),

    "^&#61927": ('There is no such user, there are only: ',
                 'TypeError Exception'
                 )
}

real_users = ['crankerkor', 'lolegoogle1',
              'LunaLovegoood', 'Yurii-Khomiak', 'dhmfu'
              ]
fake_users = ['aasdasdas', 1232, 0.1231, '^&#61927']


"""class TestSchema(unittest.TestCase):

    def test_real_user(self):
        for user in real_users:
            self.assertEqual(get_repositories(str(user)), test_data[str(user)])

    def test_fake_user(self):
        for user in fake_users:
            self.assertEqual(get_repositories(str(user)), test_data[str(user)])

"""
"""def get_repositories(login):
    url = 'https://api.github.com/graphql'
    json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % login}
    api_token = "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"
    headers = {'Authorization': 'Bearer %s' % api_token}
    try:
        response = requests.post(url=url, json=json, headers=headers)
        return response
    except TypeError as exp:
        return 'There is no such user, there are only: ', "TypeError Exception"
        
decoded_data =get_repositories("124125162135124").content.decode() 
if "NOT_FOUND" in decoded_data:
    raise KeyError

        
        """
responde = requests.post(
            url = 'https://api.github.com/graphql',
            json = {'query': '{user(login: "%s"){name repositories(first: 100){edges{node{name}}}} }' % "crankerkor"},
            headers={'Authorization': 'Bearer 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'}
        )
print(responde.json())