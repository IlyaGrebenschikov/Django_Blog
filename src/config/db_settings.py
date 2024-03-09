import os

from dotenv import load_dotenv


load_dotenv()

ENV_POSTGRES_USER = os.environ.get('POSTGRES_USER')
ENV_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
ENV_POSTGRES_DB = os.environ.get('POSTGRES_DB')
ENV_POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
ENV_POSTGRES_PORT = os.environ.get('POSTGRES_PORT')

ENV_SECRET_KEY = os.environ.get('SECRET_KEY')


if __name__ == '__main__':
    print(
        ENV_SECRET_KEY,
        ENV_POSTGRES_DB,
        ENV_POSTGRES_PORT,
        ENV_POSTGRES_HOST,
        ENV_POSTGRES_USER,
        ENV_POSTGRES_PASSWORD
    )
