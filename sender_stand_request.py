import requests
import data
import configuration


def post_new_client():
    return requests.post(configuration.URL_SERVICE + configuration.USER_SERVICE,
                         headers={"Content-Type": "application/json"},
                         json=data.user_info)


def get_auth_token():
    create_user_res = post_new_client()
    response_json = create_user_res.json()
    print(response_json)

    if "authToken" in response_json:
        configuration.AUTH_TOKEN = response_json["authToken"]


headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {configuration.AUTH_TOKEN}'
}


def check_auth_token_exist():
    if configuration.AUTH_TOKEN == None:
        get_auth_token()


def valid_kit_request(test_num):
    check_auth_token_exist()
    return requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                         headers=headers,
                         json=data.data[test_num]['kit_body'].copy())


def invalid_kit_request(test_num):
    check_auth_token_exist()
    return requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                         headers=headers,
                         json=data.data[test_num]['kit_body'].copy())
