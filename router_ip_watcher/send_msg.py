import requests

from router_ip_watcher import read_config
from router_ip_watcher import LOG, model


def send_robot(webhook, data: model.UserConfigModel):
    url = webhook
    header = {'Content-Type': 'application/json'}
    body = {
        "msgtype": "text",
        "text": {
            "content": f"{data.router.whoami}您的{data.router.device}路由器，"
                       f"在{data.result.change_time}公网ip变化为{data.result.public_ip}"
        }
    }
    res = requests.post(url=url, json=body, headers=header)
    LOG.info(f"send url={webhook}, body={body}, status_code={res.status_code}")


def main():
    user_config = read_config.get_user_config()
    robot_config = user_config.webhook
    for name, webhook in robot_config.dict().items():
        if webhook:
            send_robot(webhook, user_config)


if __name__ == '__main__':
    main()
