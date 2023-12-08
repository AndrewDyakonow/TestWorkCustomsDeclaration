from datetime import datetime, timedelta
import requests


class RequestToOzon:
    url = "https://api-seller.ozon.ru/"

    def __init__(self, api_key, client_id, request_method):
        self.api_key = api_key
        self.client_id = client_id
        self.service_url = self.url + request_method

    @property
    def headers(self):
        return {
            "Content-type": "application/json",
            "Api-Key": self.api_key,
            "Client-Id": self.client_id,
        }

    @property
    def body(self):
        return {
            "date": {
                "from": (datetime.utcnow() - timedelta(days=4)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "to": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
        }

    def request_to_ozon(self):
        responce = requests.post(url=self.service_url, headers=self.headers, json=self.body)
        return responce.json()
