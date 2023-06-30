import os
import shutil
from typing import Dict, Optional

from pydantic import BaseModel

from send_route_public_ip_robot.utils import common, file
from send_route_public_ip_robot.utils.base import PACKAGE_SHARE_DIR_NAME, PACKAGE_NAME
from send_route_public_ip_robot import LOG

config_path = '/etc/chaoshen/send-route-public-ip-robot.ini'
config_file_name = 'send-route-public-ip-robot'

user_config_path = os.path.abspath(os.path.join(common.get_chaoshen_user_config_dir(), config_file_name))


class UserConfigModel(BaseModel):
    class RouteSection(BaseModel):
        device: str
        ip: str
        username: str
        password: str

    class WebhookSection(BaseModel):
        dingtalk: Optional[str]
        wechat: Optional[str]

    class ResultSection(BaseModel):
        public_ip: Optional[str]
        change_time: Optional[str]

    route: RouteSection
    webhook: WebhookSection
    result: ResultSection


def get_default_config_path():
    base_path = common.get_current_python_share_path()
    then_path = f'{PACKAGE_SHARE_DIR_NAME}/{PACKAGE_NAME}/default_config/{config_file_name}'
    return os.path.abspath(os.path.join(base_path, then_path))


def get_config() -> UserConfigModel:
    default_config_path = get_default_config_path()
    if not os.path.exists(default_config_path):
        raise Exception(f"not find default network config, config_path={default_config_path}")

    if not os.path.exists(user_config_path):
        LOG.info('not exist user network config, copy it from default')
        shutil.copy(default_config_path, user_config_path)
    user_config = file.ini_to_dict(user_config_path)
    LOG.debug(f"user config is {user_config}")
    # network_config = {key: network.UserConfigNetworkFileModel(**value) for key, value in network_config.items()}
    user_config_model = UserConfigModel(**user_config)
    return user_config_model


if __name__ == '__main__':
    get_config()
