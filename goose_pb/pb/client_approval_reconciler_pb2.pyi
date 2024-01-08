from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientApprovalReconcilerRequest(_message.Message):
    __slots__ = ("client_name", "tagger_output", "client_feedback")
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TAGGER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    tagger_output: str
    client_feedback: str
    def __init__(self, client_name: _Optional[str] = ..., tagger_output: _Optional[str] = ..., client_feedback: _Optional[str] = ...) -> None: ...
