from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmailDocument(_message.Message):
    __slots__ = ("subject", "in_reply_to", "references", "from_email", "content", "message_id")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    IN_REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    FROM_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    subject: str
    in_reply_to: str
    references: str
    from_email: str
    content: str
    message_id: str
    def __init__(self, subject: _Optional[str] = ..., in_reply_to: _Optional[str] = ..., references: _Optional[str] = ..., from_email: _Optional[str] = ..., content: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...
