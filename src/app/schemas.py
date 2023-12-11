from pydantic import BaseModel


class Req(BaseModel):
    api_key: str
    client_id: str
