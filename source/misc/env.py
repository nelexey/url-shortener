from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    WEB_HOST: str
    WEB_PORT: int
    WEB_TIMEOUT: int
    WEB_MAX_CONNECTIONS: int


    @property
    def database_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    @property
    def web_config(self) -> dict:
        return {'host': self.WEB_HOST,
                'port': self.WEB_PORT,
                'timeout': self.WEB_TIMEOUT,
                'max_connections': self.WEB_MAX_CONNECTIONS,
                }

settings = Settings(_env_file='.env')