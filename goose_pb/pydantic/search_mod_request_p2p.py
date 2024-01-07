# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.3](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 4.25.1 
# Pydantic Version: 2.5.3 
from .email_p2p import EmailDocument
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field


class SearchModificationRequest(BaseModel):

    campaign_id: str = Field(default="") 
    instructions: str = Field(default="") 
    email_doc: EmailDocument = Field() 

