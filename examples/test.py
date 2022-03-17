# -*- coding:utf-8 -*-
import requests
import json
import base64
import os
import time

"""

python3 -m pip install requests
python3 test.py

"""

API_URL = "https://32c0w7t15f.execute-api.ap-northeast-2.amazonaws.com/Stage/enhance"
API_KEY = "<YOUR API KEY>"


def api_test(api_url, fp, out_dir='out', api_key=None):
    with open(fp, 'rb') as f:
        file_b64enc = base64.b64encode(f.read()).decode("utf8")

    request_json = {
        "config": {
            "filename": os.path.basename(fp),
        },
        "audio": {
            "content": file_b64enc,
        },
    }

    headers = {"Content-Type": "application/json; charset=UTF-8"}
    if api_key is not None:
        headers.update({
            'x-api-key': api_key
        })

    response = requests.post(
        api_url,
        headers=headers,
        json=request_json
    )

    print("[Audio IN] ", fp)
    if response.status_code != 200:
        print("[responseHeader]")
        for k, v in response.headers.items():
            print(k, v)
    else:
        data = response.json()
        out = os.path.join(out_dir, os.path.basename(fp))
        print("[Audio OUT]", out)
        with open(out, 'wb') as f:
            f.write(base64.b64decode(data['result']))
            
        print("[JSON]     ", fp + '.json')
        with open('{}.json'.format(fp), 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    src_dir = "./in"
    dst_dir = './out'

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

    if os.path.exists(src_dir):
        if os.path.isdir(src_dir):
            total_start = time.time()
            for p in os.scandir(src_dir):
                if p.name.endswith('.wav'):
                    print(f'run: {p.name}')
                    s = time.time()
                    api_test(API_URL, p.path, dst_dir, api_key=API_KEY)
                    print(f'response time:', time.time() - s, f'\n')
        else:
            total_start = time.time()
            api_test(API_URL, src_dir, dst_dir, api_key=API_KEY)
        print('total inference time:', time.time() - total_start)
