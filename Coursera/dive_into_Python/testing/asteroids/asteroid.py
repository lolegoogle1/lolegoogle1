import requests


class Asteroid:
    BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_URL.format(spk_id)
        self.data = self.get_data()

    def get_data(self):
        return requests.get(self.api_url).json()

    @property
    def name(self):
        return self.data['name']

    @property
    def diameter(self):
        return int(self.data['estimated_' +
                   'diameter']['meters']['estimated_diameter_max'])

    @property
    def closest_approach(self):
        closest = {
            'date': None,
            'distance': float('inf')
        }
        for approach in self.data['close_approach_data']:
            distance = float(approach['miss_distance']['lunar'])
            if distance < closest['distance']:
                closest.update({
                    'date': approach['close_approach_data'],
                    'distance': distance
                })
        return closest


apophis = Asteroid(2099942)

print(f'Name: {apophis.name}')
print(f'Diameter: {apophis.diameter}m')
