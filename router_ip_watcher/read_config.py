import os
import shutil
from pprint import pprint

from router_ip_watcher.utils import common, file
from router_ip_watcher.utils.base import PACKAGE_SHARE_DIR_NAME, PACKAGE_NAME
from router_ip_watcher import LOG, model


config_file_name = 'router-ip-watcher.ini'
config_path = f'/etc/chaoshen/{config_file_name}'

user_config_path = os.path.abspath(os.path.join(common.get_chaoshen_user_config_dir(), config_file_name))


def get_default_config_path():
    base_path = common.get_current_python_share_path()
    then_path = f'{PACKAGE_SHARE_DIR_NAME}/{PACKAGE_NAME}/default_config/{config_file_name}'
    return os.path.abspath(os.path.join(base_path, then_path))


def get_user_config() -> model.UserConfigModel:
    default_config_path = get_default_config_path()
    if not os.path.exists(default_config_path):
        raise Exception(f"not find default user config, config_path={default_config_path}")

    if not os.path.exists(user_config_path):
        LOG.info('not exist user network config, copy it from default')
        shutil.copy(default_config_path, user_config_path)
    LOG.info(f'read config file {user_config_path}')
    user_config = file.ini_to_dict(user_config_path)
    LOG.debug(f"user config is {user_config}")
    user_config_model = model.UserConfigModel(**user_config)
    return user_config_model


def write_user_config(user_config: model.UserConfigModel):
    LOG.info(f'write config file {user_config_path}')
    file.write_ini(user_config.dict(), user_config_path)
    return get_user_config()


def main():
    data = get_user_config()
    pprint(data.dict())


if __name__ == '__main__':
    main()
