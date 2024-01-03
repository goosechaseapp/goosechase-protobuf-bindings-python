#!/bin/bash

# Check protoc exists
if ! command -v protoc &> /dev/null
then
    echo "protoc could not be found, https://protobuf.dev/downloads/ for installation"
    exit
fi

for file in proto/*.proto
do
    # Generate the .pb.go file
    protoc -I=proto --python_out=goose_pb/pb --pyi_out=goose_pb/pb $file
done
