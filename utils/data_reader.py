import json

def load_test_data(filepath:str):

    with open(filepath,"r") as file:
        return json.load(file)