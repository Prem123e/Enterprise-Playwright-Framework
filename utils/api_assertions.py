def assert_status_code(response,expected_status_code:int):

    assert response.status_code==expected_status_code,(
        f"Expected status code {expected_status_code}, "
        f"but got {response.status_code}"
    )

def assert_json_field(response, field:str,expected_value):
    response_data=response.json()
    assert response_data[field]==expected_value,(
        f"Expected {field} to be {expected_value}, "
        f"but got {response_data[field]}"
    )