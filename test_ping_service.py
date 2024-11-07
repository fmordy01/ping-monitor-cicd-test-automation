import logging
from ping_service import ping_host

logging.basicConfig(level=logging.INFO)


def test_ping_host_up_one():
    assert ping_host("https://www.google.com") == True  # expected output: up


def test_ping_host_up_two():
    # expected output: up
    assert ping_host("https://www.cloudflare.com") == True


def test_ping_host_down():
    # expected output: down
    assert ping_host("https://doesntexist.something.down.test.com") == False
