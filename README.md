# Protobuf Python Binding

`goose_pb/pb` contains runtime classes and their stubs`.
`goose_pb/pydantic` contains pydantic models generated from protobuf.

## Generation

```bash
chmod +x ./generate.sh
poetry shell
./generate.sh
```

## Notes

* make sure `goose_pb/pydantic/__init__.py` is correct after generation.
* ignore the import errors in proto files.