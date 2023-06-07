import requests

def test1():
    session = requests.Session()
    # ruleid: request-session-with-http
    session.get("http://example.com")

def test1_ok():
    session = requests.Session()
    # ok: request-session-with-http
    session.get("https://example.com")

def test2():
    session = requests.Session()
    url = "http://example.com"
    # ruleid: request-session-with-http
    session.post(url)

def test2_ok():
    session = requests.Session()
    # ok: request-session-with-http
    url = "https://example.com"
    session.post(url)

def test3(url = "http://example.com"):
    session = requests.Session()
    # ruleid: request-session-with-http
    session.delete(url)

def test3_ok(url = "https://example.com"):
    session = requests.Session()
    # ok: request-session-with-http
    session.delete(url)

def test4(url = "http://example.com"):
    session = requests.Session()
    # ruleid: request-session-with-http
    session.request("HEAD", url, timeout=30)

def test4_ok(url = "https://example.com"):
    session = requests.Session()
    # ok: request-session-with-http
    session.request("HEAD", url, timeout=30)

def test_localhost_ok(url = "http://localhost/blah"):
    session = requests.Session()
    # ok: request-session-with-http
    session.request("HEAD", url, timeout=30)

def test_localhost_ok2(url = "http://127.0.0.1/blah"):
    session = requests.Session()
    # ok: request-session-with-http
    session.request("HEAD", url, timeout=30)