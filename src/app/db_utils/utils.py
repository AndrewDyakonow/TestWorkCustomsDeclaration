from src.app.db_utils.model import Declaration
from src.db_config import settings, session
from clickhouse_sqlalchemy.exceptions import DatabaseException
from sqlalchemy import text


def insert_or_create_table(data: list) -> str:
    """
        Создаёт таблицу в БД, если её нет, и сохраняет данные
    :param data: Список словарей с данными по декларациям
    :return: Сообщение об успешной записи
    """
    list_data = [{
        "posting_number": i.get("posting_number"),
        "etgb_number": i.get("etgb").get("number"),
        "etgb_date": i.get("etgb").get("date"),
        "etgb_url": i.get("etgb").get("url"),
    } for i in data]

    try:
        session.execute(Declaration.__table__.insert(), list_data)
    except DatabaseException:
        Declaration.__table__.create(settings.engine)
        session.execute(Declaration.__table__.insert(), list_data)
    finally:
        session.execute(text('OPTIMIZE TABLE declaration FINAL;'))
        session.commit()
        session.close()
        return 'Декларации сохранены'
