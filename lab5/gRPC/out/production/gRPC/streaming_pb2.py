# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fstreaming.proto\x12\tstreaming\"\x13\n\x04Task\x12\x0b\n\x03max\x18\x01 \x01(\x05\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x05\".\n\x06Report\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x15\n\rprocessorTime\x18\x02 \x01(\x03\x32\x8d\x01\n\x0cStreamTester\x12>\n\x14GeneratePrimeNumbers\x12\x0f.streaming.Task\x1a\x11.streaming.Number\"\x00\x30\x01\x12=\n\x11\x43ountPrimeNumbers\x12\x11.streaming.Number\x1a\x11.streaming.Report\"\x00(\x01\x42\x1f\n\x0bsr.grpc.genB\x0eStreamingProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streaming_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013sr.grpc.genB\016StreamingProtoP\001'
  _globals['_TASK']._serialized_start=30
  _globals['_TASK']._serialized_end=49
  _globals['_NUMBER']._serialized_start=51
  _globals['_NUMBER']._serialized_end=74
  _globals['_REPORT']._serialized_start=76
  _globals['_REPORT']._serialized_end=122
  _globals['_STREAMTESTER']._serialized_start=125
  _globals['_STREAMTESTER']._serialized_end=266
# @@protoc_insertion_point(module_scope)
