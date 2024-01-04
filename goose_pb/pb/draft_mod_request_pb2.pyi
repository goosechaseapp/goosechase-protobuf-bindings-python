import email_pb2 as _email_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DraftModificationRequest(_message.Message):
    __slots__ = ("campaign_id", "instructions", "email_doc")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOC_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    instructions: str
    email_doc: _email_pb2.EmailDocument
    def __init__(self, campaign_id: _Optional[str] = ..., instructions: _Optional[str] = ..., email_doc: _Optional[_Union[_email_pb2.EmailDocument, _Mapping]] = ...) -> None: ...
