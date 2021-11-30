import requests

if __name__ == '__main__':
    url = 'https://hal.archives-ouvertes.fr/search/index/'
    # send requests with paras
    query = input('what do you want to research :  ')
    param = {
        'q': query
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    # get data form of string
    page_text = response.text
    # stock data
    with open('./HAL-Inria_test.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print("finish process!")
