import requests

from send_route_public_ip_robot import LOG
from send_route_public_ip_robot import read_config

user_config = read_config.get_user_config()


def get_cookie():
    route_config = user_config.route
    login_url = 'http://{}/cgi-bin/luci'.format(route_config.ip)
    session = requests.session()
    session.post(login_url, data={'username': route_config.username, 'psd': route_config.password})
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    if not html_set_cookie:
        err = "get cookie failed, check you route login account"
        LOG.exception(err)
        raise Exception(err)
    LOG.info(f'get cookie is {html_set_cookie}')
    return session, html_set_cookie


def get_public_ip():
    session, cookie = get_cookie()
    url = 'http://{}/cgi-bin/luci/admin/settings/gwinfo?get=part'.format(user_config.route.ip)
    LOG.debug(f'get url {url}')
    res = session.get(url, cookies=cookie)
    if res.status_code // 100 != 2:
        err = "get setting failed, maybe cookie is error"
        LOG.exception(err)
        raise Exception(err)
    data = res.json()
    wan_ip = data.get('WANIP')
    LOG.info(f'public ip is {wan_ip}')


def main():
    get_public_ip()


if __name__ == '__main__':
    main()
