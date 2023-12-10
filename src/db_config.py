from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine, MetaData
from src.global_settings import ENV_PATH
from clickhouse_sqlalchemy import make_session


class Settings(BaseSettings):
    """Модель настроек подключения к БД"""
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=ENV_PATH)

    @property
    def engine(self):
        """Движок для подключения к БД"""
        uri = f"clickhouse+http://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        result = create_engine(url=uri, echo=False)
        return result


settings = Settings()
metadata_obj = MetaData()
session = make_session(settings.engine)
