# frozen_string_literal: true
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming.proto

require 'google/protobuf'


descriptor_data = "\n\x0fstreaming.proto\x12\tstreaming\"\x13\n\x04Task\x12\x0b\n\x03max\x18\x01 \x01(\x05\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x05\".\n\x06Report\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x15\n\rprocessorTime\x18\x02 \x01(\x03\x32\x8d\x01\n\x0cStreamTester\x12>\n\x14GeneratePrimeNumbers\x12\x0f.streaming.Task\x1a\x11.streaming.Number\"\x00\x30\x01\x12=\n\x11\x43ountPrimeNumbers\x12\x11.streaming.Number\x1a\x11.streaming.Report\"\x00(\x01\x42\x1f\n\x0bsr.grpc.genB\x0eStreamingProtoP\x01\x62\x06proto3"

pool = Google::Protobuf::DescriptorPool.generated_pool
pool.add_serialized_file(descriptor_data)

module Streaming
  Task = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("streaming.Task").msgclass
  Number = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("streaming.Number").msgclass
  Report = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("streaming.Report").msgclass
end
