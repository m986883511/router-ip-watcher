# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import time

route_ip = '192.168.1.1'

login_url = 'http://{}/cgi-bin/luci'.format(route_ip)

session = requests.session()
session.post(login_url, data={'username': 'useradmin', 'psd': 'jxfmm'})
html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
print(html_set_cookie)

start_time = time.time()
while True:
    url = 'http://{}/cgi-bin/luci/admin/settings/gwinfo?get=part'.format(route_ip)
    html = session.get(url, cookies=html_set_cookie)
    print(html.text)
    time.sleep(1)
    print(time.time() - start_time)


class Base:
    pass


def main():
    print("hello world")


if __name__ == '__main__':
    main()
