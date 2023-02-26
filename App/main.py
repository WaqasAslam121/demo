from fastapi import FastAPI


app = FastAPI()

@app.get('/demo')
def get_demo():
    return 'Hello World'