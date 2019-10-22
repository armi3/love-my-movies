import requests


@staticmethod
def get_list(app, call):
    url = call + app.config['API_KEY']
    r = requests.get(url)
    print(r.status_code)
    print(r.json())
    print(type(r.json()))
    return r.json()
