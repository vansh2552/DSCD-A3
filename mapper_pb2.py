# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mapper.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmapper.proto\"&\n\x11partitionResponse\x12\x11\n\tpartition\x18\x01 \x01(\t\":\n\x15\x63\x65ntroidUpdateRequest\x12\x0e\n\x06points\x18\x01 \x03(\x05\x12\x11\n\tcentroids\x18\x02 \x01(\t2N\n\rMapperService\x12=\n\x0fReceiveCentroid\x12\x16.centroidUpdateRequest\x1a\x12.partitionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mapper_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PARTITIONRESPONSE']._serialized_start=16
  _globals['_PARTITIONRESPONSE']._serialized_end=54
  _globals['_CENTROIDUPDATEREQUEST']._serialized_start=56
  _globals['_CENTROIDUPDATEREQUEST']._serialized_end=114
  _globals['_MAPPERSERVICE']._serialized_start=116
  _globals['_MAPPERSERVICE']._serialized_end=194
# @@protoc_insertion_point(module_scope)
