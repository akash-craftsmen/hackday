import requests

def get_request(url, headers=None, data=None):
    response = requests.get(url, headers=headers, json=data)


def post_request(url, headers=None, data=None):
    response = requests.post(url, headers=headers, json=data)
