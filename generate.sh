#!/bin/bash

for file in proto/*.proto
do
    poetry run python -m grpc_tools.protoc -I ./proto --protobuf-to-pydantic_out=./goose_pb/pydantic $file 
done
