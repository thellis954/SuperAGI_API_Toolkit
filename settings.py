from dataclasses import dataclass

@dataclass
class Settings:
    API_URL: str
    USERNAME: str
    PASSWORD: str
    ACCESS_TOKEN: str

def load_settings():
    # Load settings from configuration file or environment variables
    settings = Settings(
        API_URL='https://webservices.mss1.com/MSSSubconAPI/',
        USERNAME='username',
        PASSWORD='password',
        ACCESS_TOKEN='access_token'
    )
    return settings
