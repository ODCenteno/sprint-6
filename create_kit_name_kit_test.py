import data
import sender_stand_request


def test_kit_creation_with_min_length_name():
    response = sender_stand_request.valid_kit_request('test_1')
    json_res = response.json()
    print(json_res)
    assert response.status_code == 201
    assert json_res['name'] == data.data['test_1']['kit_body']['name']


def test_max_characters_allowed_for_user_name_is_511():
    response = sender_stand_request.valid_kit_request('test_2')
    json_res = response.json()
    assert response.status_code == 201
    assert json_res['name'] == data.data['test_2']['kit_body']['name']


def test_invalid_characters_length_is_cero():
    response = sender_stand_request.invalid_kit_request('test_3')
    assert response.status_code == 400


def test_invalid_characters_length_over_max_eq_512():
    response = sender_stand_request.invalid_kit_request('test_4')
    assert response.status_code == 400


def test_valid_use_of_special_characters_for_kit_name():
    response = sender_stand_request.valid_kit_request('test_5')
    json_res = response.json()
    print(json_res)
    assert response.status_code == 201
    assert json_res['name'] == data.data['test_5']['kit_body']['name']


def test_valid_use_of_spaces_in_kit_name():
    response = sender_stand_request.valid_kit_request('test_6')
    json_res = response.json()

    assert response.status_code == 201
    assert json_res['name'] == data.data['test_6']['kit_body']['name']


def test_valid_use_of_numbers_in_kit_name():
    response = sender_stand_request.valid_kit_request('test_7')
    json_res = response.json()

    assert response.status_code == 201
    assert json_res['name'] == data.data['test_7']['kit_body']['name']


def test_invalid_request_no_param_name_is_passed():
    response = sender_stand_request.invalid_kit_request('test_8')
    assert response.status_code == 400


def test_invalid_data_type_for_name_param_a_number_is_passed():
    response = sender_stand_request.invalid_kit_request('test_9')
    assert response.status_code == 400
