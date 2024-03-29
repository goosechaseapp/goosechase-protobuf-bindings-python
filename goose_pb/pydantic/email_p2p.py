# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 4.25.1 
# Pydantic Version: 2.5.3 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field


class EmailDocument(BaseModel):

    subject: str = Field(default="") 
    in_reply_to: str = Field(default="") 
    references: str = Field(default="") 
    from_email: str = Field(default="") 
    content: str = Field(default="") 
    message_id: str = Field(default="") 


class SendEmailDocument(BaseModel):

    to_address: str = Field(default="") 
    received_email: EmailDocument = Field() 

