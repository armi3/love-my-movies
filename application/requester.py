import requests


@staticmethod
def get_info(app, db, list_id):
    # check for list in redis cache
    if db.exists(list_id):
        # next refactor: check for changes/updates here
        return db.get(list_id)
    else:
        # if not cached, request from API
        json = get_from_api(app, list_id)
        set_from_json(json)
        return db.get(list_id)


def get_from_api(app, list_id):
    call = 'https://api.themoviedb.org/3/list/' + list_id + '?api_key='
    url = call + app.config['API_KEY']
    r = requests.get(url)
    print(r.status_code)
    print(r.json())
    print(type(r.json()))
    return r.json()


def set_from_json(db, json, list_id):
    db.set(list_id, json['name'])                               # name
    db.set(list_id+'item_count', json['item_count'])            # item_count
    db.set(list_id + 'item_count', json['item_count'])
