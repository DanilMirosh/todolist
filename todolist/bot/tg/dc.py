from pydantic import BaseModel, Field


class MessageFrom(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: str


class Chat(BaseModel):
    id: int
    first_name: str
    username: str
    type: str


class Message(BaseModel):
    message_id: int
    from_: MessageFrom = Field(..., alias='from')
    chat: Chat
    date: int
    text: str

    class Config:
        allow_population_by_field_name = True


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdatesResponse(BaseModel):
    ok: bool
    result: list[UpdateObj] = []


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message
