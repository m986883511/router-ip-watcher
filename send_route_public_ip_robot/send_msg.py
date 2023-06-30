import requests

from send_route_public_ip_robot import read_config
from send_route_public_ip_robot import LOG

def fun(webhook):
    url = webhook
    header = {'Content-Type': 'application/json'}
    body = {
        "msgtype": "text",
        "text": {
            "content": "路由器ip变更为180.5.5.5"
        }
    }
    # 注意：json=mBody  必须用json
    res = requests.post(url=url, json=body, headers=header)
    LOG.info(f"send url={webhook} result is {res.status_code}")


def main():
    user_config = read_config.get_user_config()
    robot_config = user_config.webhook
    for name, webhook in robot_config.dict().items():
        if webhook:
            fun(webhook)


if __name__ == '__main__':
    main()
