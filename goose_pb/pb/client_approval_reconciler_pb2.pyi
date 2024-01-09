import email_pb2 as _email_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientApprovalReconcilerRequest(_message.Message):
    __slots__ = ("client_name", "tagger_output", "client_feedback", "email_doc", "send_to")
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TAGGER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOC_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    tagger_output: str
    client_feedback: str
    email_doc: _email_pb2.EmailDocument
    send_to: str
    def __init__(self, client_name: _Optional[str] = ..., tagger_output: _Optional[str] = ..., client_feedback: _Optional[str] = ..., email_doc: _Optional[_Union[_email_pb2.EmailDocument, _Mapping]] = ..., send_to: _Optional[str] = ...) -> None: ...
