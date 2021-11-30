import json

import requests

if __name__ == '__main__':
    url = 'https://hal.archives-ouvertes.fr/search/index/'
    # send requests
    #response = requests.get(url=url)
    # get data form of string
    # page_text = response.text
    # stock data
    # with open('./HAL-Inria.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)

    param = {
        'q': 'image'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    # print(response.json())
    # list_data = response.json()
    with open('./HAL-Inria.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    # fp = open('./HAL-Inria.json', 'w', encoding='utf-8')
    # json.dump(list_data, fp=fp, ensure_ascii=False)

    print("finish process!")
