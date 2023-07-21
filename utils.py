def process_response(response):
    if response.status_code == 200:
        print('Request successful')
        print(response.json())
    else:
        print('Request failed')
        print(response.text)
