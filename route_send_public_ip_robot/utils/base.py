from enum import Enum

# 放在用户目录下载的文件，里面可以放自定义的配置文件
USER_CONFIG_DIR_NAME = '.chaoshen'
# 包安装的时候会自动将一些文件放在python环境的share目录
PACKAGE_SHARE_DIR_NAME = 'chaoshen-toolbox'
PACKAGE_NAME = 'route_send_public_ip_robot'


class Platform(Enum):
    windows = ['win7', 'win10']
    linux = ['fedora']


config_ip_support_platform = [Platform.windows.name, Platform.linux.name]
