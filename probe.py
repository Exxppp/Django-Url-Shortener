import requests
from faker import Faker

fake = Faker()
r = requests.session()
base_location = 'http://localhost:8001'
location = base_location + '/links/create/'
login_location = base_location + '/login/'
r.request('get', login_location, data={
    'username': 'ZzbRtz',
    'password': 'wsdeaq231',
})

for i in range(40):
    r.request('post', location, json={
        'url': f'https://localhost:8000/{fake.pystr()}'
    })
