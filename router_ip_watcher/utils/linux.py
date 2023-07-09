import os
import logging

LOG = logging.getLogger(__name__)

from router_ip_watcher.utils import common, base


def check_is_root():
    flag = os.geteuid() == 0
    if not flag:
        LOG.warning("current user not have root permission")
    return flag


def create_service(service_name, service_content):
    service_path = f'/etc/systemd/system/{service_name}.service'
    if os.path.exists(service_path):
        LOG.warning(f'{service_path} already exists, skip create')
        return
    with open(service_path, 'w') as f:
        f.write(service_content)
    LOG.info(f'create {service_path} success')


class LinuxService:

    def __init__(self, service_name, run_command, description=None, user='root'):
        self.service_name = service_name
        self.run_command = run_command
        self.service_filepath = f'/etc/systemd/system/{service_name}.service'
        description = description or service_name
        self.content = f"""
[Unit]
Description={description}

[Service]
Type=simple
TimeoutStartSec=0
Restart=always
User={user}
ExecStart={run_command}

[Install]
WantedBy=multi-user.target
"""

    def create_service_file(self):
        common.check_current_platform_is_correct(base.Platform.linux.name)
        with open(self.service_filepath, 'w') as f:
            f.write(self.content)
        LOG.info(f'create {self.service_filepath} success')
