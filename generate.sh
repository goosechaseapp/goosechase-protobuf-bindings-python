#!/bin/bash

# Delete old files in pb and pydantic
rm -rf goose_pb/pb/*.py
rm -rf goose_pb/pb/*.pyi

# delete *_p2p.py files
rm -rf goose_pb/pydantic/*_p2p.py

for file in proto/*.proto
do
    poetry run python -m grpc_tools.protoc -I ./proto --python_out=goose_pb/pb --pyi_out=goose_pb/pb  --protobuf-to-pydantic_out=./goose_pb/pydantic $file 
done
