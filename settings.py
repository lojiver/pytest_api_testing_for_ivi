from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    base_url: str = Field(..., env='BASE_URL')
    user_email: str = Field(..., env='TEST_USER_EMAIL')
    user_password: str = Field(..., env='TEST_USER_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'

    @property
    def user(self) -> tuple:
        return (self.user_email, self.user_password)


base_settings = Settings()
