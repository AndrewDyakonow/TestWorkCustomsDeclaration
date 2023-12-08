from pprint import pprint
from fastapi import FastAPI
from app.logic import RequestToOzon

app = FastAPI()


@app.post('/')
def get_data(api_key: str, client_id: str):
    request_method = "v1/posting/global/etgb"
    request_obj = RequestToOzon(api_key, client_id, request_method)
    pprint(request_obj.request_to_ozon())
    return "Good"
