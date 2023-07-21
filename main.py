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

    data = {'key': 'value'}
    response = client.post('/endpoint', data)
    utils.process_response(response)

if __name__ == '__main__':
    main()
