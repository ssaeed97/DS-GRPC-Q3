from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRequest(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("status", "timestamp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: str
    timestamp: str
    def __init__(self, status: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...
