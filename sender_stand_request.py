from data import user_info as user
import requests
import data
import configuration


def post_new_client():
    return requests.post(configuration.URL_SERVICE + configuration.USER_SERVICE,
                         headers={"Content-Type": "application/json"},
                         json=user)


def get_auth_token():
        create_user_res = post_new_client()
        response_json = create_user_res.json()

        if "authToken" in response_json:
            return response_json["authToken"]
        else:
            return None


headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {get_auth_token()}'
}

def kit_request(test_num):
    return requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                         headers=headers,
                         json=data.data[test_num]['kit_body'].copy())
