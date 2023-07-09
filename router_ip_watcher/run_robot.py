import time

from router_ip_watcher import LOG, read_config, calc_public_ip, send_msg
from router_ip_watcher.utils import common


def main():
    while True:
        try:
            user_config = read_config.get_user_config()
            interval = user_config.router.interval
            cookie = calc_public_ip.get_cookie()
            LOG.info('start get public ip')
            while True:
                public_ip = calc_public_ip.get_public_ip(cookie)
                if public_ip != user_config.result.public_ip:
                    user_config.result.public_ip = public_ip
                    user_config.result.change_time = common.get_beijing_time()
                    user_config = read_config.write_user_config(user_config)
                    send_msg.main()
                    LOG.info(f'public ip change to {public_ip}')
                time.sleep(interval)
        except Exception as e:
            LOG.exception(f"get router login cookie failed, wait 60 seconds to retry, err={str(e)}")
            time.sleep(60)


if __name__ == '__main__':
    main()
