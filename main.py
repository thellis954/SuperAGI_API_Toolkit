import settings
import api_client
import utils

def main():
    # Load settings from configuration file
    settings.load_settings()

    # Create API client
    client = api_client.APIClient(settings.API_URL, settings.USERNAME, settings.PASSWORD, settings.ACCESS_TOKEN)

    # Perform API requests
    response = client.get('/endpoint')
    utils.process_response(response)
    ACCESS_TOKEN = utils.process_response(client.post(f"{client.api_url}/login",f"{client.username}|{client.password}"))

    print(ACCESS_TOKEN)
    data = {'key': 'value'}
    response = client.post('/endpoint', data)
    utils.process_response(response)

if __name__ == '__main__':
    main()
