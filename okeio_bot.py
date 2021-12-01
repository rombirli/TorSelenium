from threading import Thread

from ntorlib.ntorlib import create_n_dependencies, clean_dependencies, run_1_tor, get_proxy, run_n_tor
import sys
import requests

NTHREADS = 8

from torpy.http.requests import TorRequests, tor_requests_session


def click_1(i):
    from urllib import request
    with tor_requests_session() as s:
        print(s.get('https://anti-captcha.com/?campaign=allwords&gclid=Cj0KCQiAtJeNBhCVARIsANJUJ2Fh-Vas5Y1te7C631_tzs2Q4XJpnWiXqyeID2zJIAUQ42GHOUhOkE0aAqLgEALw_wcB').text)


def click_n(i, n=10000):
    for _ in range(n):
        click_1(i)


proxies = {
    "http": "socks://127.0.0.1:9050",
    "https": "socks://127.0.0.1:9050"
}
create_n_dependencies(1)
tor_process = run_1_tor(0)
click_1(0)
# tor_process.kill()
print(requests.get('https://oke.io/').text)
