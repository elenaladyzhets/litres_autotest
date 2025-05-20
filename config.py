from typing import Literal, cast
from utils import tools
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

Context = Literal['local_emulator', 'bstack']


class Config(BaseSettings):
    context: Context = 'local_emulator'
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    app: str
    platformVersion: str = ''
    deviceName: str = ''
    udid: str = ''
    remote_url: str = ''
    timeout: float = 10.0

    model_config = SettingsConfigDict(env_file_encoding='utf-8')


def load_config():
    credentials_path = tools.path_to_env('.env.credentials')
    load_dotenv(dotenv_path=credentials_path)

    raw_context = os.getenv('context', 'bstack')
    context: Context = cast(Context, raw_context)


    env_path = tools.path_to_env(f'.env.{context}')
    load_dotenv(dotenv_path=env_path)


    env_vars = {
        'context': context,
        'app': os.getenv('app'),
        'deviceName': os.getenv('deviceName'),
        'platformVersion': os.getenv('platformVersion'),
        'remote_url': os.getenv('remote_url'),
        'udid': os.getenv('udid', ''),
        'bstack_userName': os.getenv('bstack_userName'),
        'bstack_accessKey': os.getenv('bstack_accessKey')
    }

    return Config(**env_vars)


config = load_config()
