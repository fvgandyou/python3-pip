import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    # print(r.text) # Its a string

    categories = r.json()
    total_categories = []
    for category in categories:
        # print(category['name'])
        total_categories.append(category['name'])
    return total_categories
