# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft_mod_request.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import email_pb2 as email__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64raft_mod_request.proto\x12\x1bgoosechase.data.draftmodreq\x1a\x0b\x65mail.proto\"~\n\x18\x44raftModificationRequest\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x14\n\x0cinstructions\x18\x02 \x01(\t\x12\x37\n\temail_doc\x18\x03 \x01(\x0b\x32$.goosechase.data.email.EmailDocumentB\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'draft_mod_request_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007./proto'
  _globals['_DRAFTMODIFICATIONREQUEST']._serialized_start=69
  _globals['_DRAFTMODIFICATIONREQUEST']._serialized_end=195
# @@protoc_insertion_point(module_scope)
