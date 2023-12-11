from fastapi import FastAPI
from aiohttp.client_exceptions import ContentTypeError
from src.app.db_utils.utils import insert_or_create_table
from src.app.logic import RequestToOzon
# from testes import test_data                                      # Тестовые данные
from src.app.schemas import Req

app = FastAPI(title='Customs declarations')


@app.post('/')
async def get_data(datas: Req):
    """Получить декларации и записать в БД"""
    request_method = "v1/posting/global/etgb"
    request_obj = RequestToOzon(datas.api_key, datas.client_id, request_method)

    try:
        data = await request_obj.request_to_ozon()
        # data = test_data                                          # Тестовые данные
        if data.get('result'):
            status = insert_or_create_table(data['result'])
        elif data.get('message'):
            status = "Предоставлены неверные данные"
        else:
            status = "Деклараций не найдено"
    except ContentTypeError as messages:
        status = messages.message

    return status
