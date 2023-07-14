import requests

from router_ip_watcher import LOG
from router_ip_watcher import read_config

user_config = read_config.get_user_config()


def get_cookie():
    router_config = user_config.router
    login_url = 'http://{}/cgi-bin/luci'.format(router_config.ip)
    session = requests.session()
    data = {'username': router_config.username, 'psd': router_config.password}
    res = session.post(login_url, data=data)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    if not html_set_cookie:
        err = f"get cookie failed, check you router login account, " \
              f"url={login_url}, data={data}, status_code={res.status_code}, res.text={res.text}"
        LOG.exception(err)
        raise Exception(err)
    LOG.info(f'get cookie is {html_set_cookie}')
    return html_set_cookie


def get_wan_ip(cookie=None):
    cookie = cookie or get_cookie()
    url = 'http://{}/cgi-bin/luci/admin/settings/gwinfo?get=part'.format(user_config.router.ip)
    LOG.debug(f'get url {url}')
    res = requests.session().get(url, cookies=cookie)
    if res.status_code // 100 != 2:
        err = "get setting failed, maybe cookie is error"
        LOG.exception(err)
        raise Exception(err)
    data = res.json()
    wan_ip = data.get('WANIP')
    LOG.info(f'wan ip is {wan_ip}')
    return wan_ip


def main():
    get_wan_ip()


if __name__ == '__main__':
    main()
