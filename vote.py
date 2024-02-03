import time
import requests
import json
import random

votecount = 0

def get_ran_number():
    return random.randint(10000000, 99999999)

def api_call(url, body, auth=None, method='POST'):
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json;charset=UTF-8',
        'Referer': "https://i-newgen.moserv.co.th/highschool",
        'Sec-Ch-UA': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-UA-Mobile': '?0',
        'Sec-Ch-UA-Platform': '"Windows"',
    }
    response = requests.request(method, url, headers=headers, data=json.dumps(body))
    print()
    print("Logs Below :")
    print(response.status_code)
    print(response.text)  # Print or log the response content

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle errors as needed

# Example usage with your specific data structure and query parameter
params = {
    'status': 1,
    'education': "",
    'code': "16011",
    'project': "ไฮโดรเซนส์ – อุปกรณ์ช่วยดักจับโลหะหนักในน้ำเสียก่อนการระบาย โดยใช้เส้นผม",
    'institute': "โรงเรียนอัสสัมชัญธนบุรี",
    'user-agent': "VoteAuto"
}

while True:
    query_param_r = get_ran_number()
    url = f'https://i-newgen.moserv.co.th/vote?r={query_param_r}'
    response_data_str = api_call(url, params)

    try:
        response_data = json.loads(response_data_str)
        print()
        if response_data and response_data.get('status') == 'ok':
            votecount = votecount + 1
            print('Vote successful')
            print("Votes : " + str(votecount))
        else:
            print('Vote failed')
            print("Votes : " + str(votecount))
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')

