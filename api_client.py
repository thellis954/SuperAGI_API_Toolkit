import requests

class APIClient:
    def __init__(self, api_url, username, password, access_token):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.access_token = access_token

    def get(self, endpoint):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        url = f'{self.api_url}{endpoint}'
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, data):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        url = f'{self.api_url}{endpoint}'
        response = requests.post(url, headers=headers, json=data)
        return response
