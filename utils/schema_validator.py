def validate_post_schema(response_data: dict):

    assert isinstance(response_data["userId"], int)
    assert isinstance(response_data["id"], int)
    assert isinstance(response_data["title"], str)
    assert isinstance(response_data["body"], str)