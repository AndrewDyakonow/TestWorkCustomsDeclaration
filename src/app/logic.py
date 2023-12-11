from datetime import datetime, timedelta
import aiohttp


class RequestToOzon:
    """Запрос на API Озон"""
    url = "https://api-seller.ozon.ru/"

    def __init__(self, api_key, client_id, request_method):
        self.api_key = api_key
        self.client_id = client_id
        self.service_url = self.url + request_method

    @property
    def headers(self) -> dict:
        """Заголовок запроса"""
        return {
            "Content-type": "application/json",
            "Api-Key": self.api_key,
            "Client-Id": self.client_id,
        }

    @property
    def body(self) -> dict:
        """Тело запроса"""
        return {
            "date": {
                "from": (datetime.utcnow() - timedelta(days=4)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "to": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
        }

    async def request_to_ozon(self):
        """Запрос"""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.service_url,
                headers=self.headers,
                json=self.body
            ) as resp:
                responce = await resp.json()
        return responce
