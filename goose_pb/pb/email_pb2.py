# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: email.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65mail.proto\x12\x15goosechase.data.email\"\x82\x01\n\rEmailDocument\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0bin_reply_to\x18\x02 \x01(\t\x12\x12\n\nreferences\x18\x03 \x01(\t\x12\x12\n\nfrom_email\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\t\"e\n\x11SendEmailDocument\x12\x12\n\nto_address\x18\x01 \x01(\t\x12<\n\x0ereceived_email\x18\x02 \x01(\x0b\x32$.goosechase.data.email.EmailDocumentB\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'email_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007./proto'
  _globals['_EMAILDOCUMENT']._serialized_start=39
  _globals['_EMAILDOCUMENT']._serialized_end=169
  _globals['_SENDEMAILDOCUMENT']._serialized_start=171
  _globals['_SENDEMAILDOCUMENT']._serialized_end=272
# @@protoc_insertion_point(module_scope)
