import json

from jsonschema import validate

def validate_schema(response_data:dict,schema_file:str):
    with open(schema_file,"r") as  file:
        schema=json.load(file)
    validate(
        instance=response_data,
        schema=schema
    )