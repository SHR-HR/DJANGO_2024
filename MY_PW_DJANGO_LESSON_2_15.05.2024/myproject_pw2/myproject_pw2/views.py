import requests

def fetch_data_from_api():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json() if response.status_code == 200 else []
    return todos

from django.http import HttpResponse

def display_todos_console(request):
    todos = fetch_data_from_api()
    for todo in todos:
        print(todo)
    return HttpResponse("Data has been printed to the console.")

def display_todos_web(request):
    todos = fetch_data_from_api()
    output = '<br>'.join([str(todo) for todo in todos])
    return HttpResponse(output)
