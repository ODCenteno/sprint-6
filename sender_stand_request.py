from data import user_info as user
import requests
import data
import configuration


def post_new_client():
    return requests.post(configuration.URL_SERVICE + configuration.USER_SERVICE,
                         headers={"Content-Type": "application/json"},
                         json=user)


def get_auth_token():
        if configuration.AUTH_TOKEN != None:
            return configuration.AUTH_TOKEN
        else:
            create_user_res = post_new_client()
            response_json = create_user_res.json()
            configuration.AUTH_TOKEN = response_json["authToken"]
            return response_json["authToken"]


headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {get_auth_token()}'
}

def kit_request(test_num):
    return requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                         headers=headers,
                         json=data.data[test_num]['kit_body'].copy())
