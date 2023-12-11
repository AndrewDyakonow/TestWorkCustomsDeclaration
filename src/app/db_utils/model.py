from sqlalchemy import Column
from clickhouse_sqlalchemy import get_declarative_base, types, engines
from src.db_config import metadata_obj

Base = get_declarative_base(metadata=metadata_obj)


class Declaration(Base):
    """Модель Декларации"""
    posting_number = Column(types.String, primary_key=True)
    etgb_number = Column(types.String)
    etgb_date = Column(types.String)
    etgb_url = Column(types.String)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(etgb_number,)
        ),
    )
