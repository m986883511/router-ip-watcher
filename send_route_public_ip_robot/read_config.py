import os
import shutil
from pprint import pprint
from typing import Optional

from pydantic import BaseModel

from send_route_public_ip_robot.utils import common, file
from send_route_public_ip_robot.utils.base import PACKAGE_SHARE_DIR_NAME, PACKAGE_NAME
from send_route_public_ip_robot import LOG

config_path = '/etc/chaoshen/send-route-public-ip-robot.ini'
config_file_name = 'send-route-public-ip-robot.ini'

user_config_path = os.path.abspath(os.path.join(common.get_chaoshen_user_config_dir(), config_file_name))


class UserConfigModel(BaseModel):
    class _RouteSection(BaseModel):
        whoami: str
        device: str
        ip: str
        username: str
        password: str

    class _WebhookSection(BaseModel):
        dingtalk: Optional[str]
        wechat: Optional[str]

    class _ResultSection(BaseModel):
        public_ip: Optional[str]
        change_time: Optional[str]

    route: _RouteSection
    webhook: _WebhookSection
    result: _ResultSection


def get_default_config_path():
    base_path = common.get_current_python_share_path()
    then_path = f'{PACKAGE_SHARE_DIR_NAME}/{PACKAGE_NAME}/default_config/{config_file_name}'
    return os.path.abspath(os.path.join(base_path, then_path))


def get_user_config() -> UserConfigModel:
    default_config_path = get_default_config_path()
    if not os.path.exists(default_config_path):
        raise Exception(f"not find default network config, config_path={default_config_path}")

    if not os.path.exists(user_config_path):
        LOG.info('not exist user network config, copy it from default')
        shutil.copy(default_config_path, user_config_path)
    LOG.info(f'read config file {user_config_path}')
    user_config = file.ini_to_dict(user_config_path)
    LOG.debug(f"user config is {user_config}")
    user_config_model = UserConfigModel(**user_config)
    return user_config_model


def main():
    data = get_user_config()
    pprint(data.dict())


if __name__ == '__main__':
    main()
