from sqlalchemy .ext.declarative import declarative_base

Base = declarative_base


import requests

x = requests.get('https://w3schools.com')
print(x.status_code)
