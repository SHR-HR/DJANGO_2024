import requests

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        return response.json()
    return []

def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return response.json()
    return []
