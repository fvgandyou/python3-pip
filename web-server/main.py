import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') # Open home
def get_list():
    return store.get_categories()

@app.get('/contact') # Create new pages
def get_list():
    return {'name': 'Monty'}

@app.get('/abstract', response_class=HTMLResponse) # Insert HTML
def get_list():
    return '''
        <h1>Hey, I'm a page</h1>
        <p>I'm a pragraph</p>
    '''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()