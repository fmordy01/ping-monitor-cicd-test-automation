import logging
import requests


logging.basicConfig(level=logging.INFO)


def ping_host(url):
    try:
        response = requests.get(url, timeout=1)

        if response.status_code == 200:
            logging.info(f"{url} is UP")
            return True
        else:
            logging.info(f"{url} is DOWN - Status: {response.status_code}")
            return False

    except requests.ConnectionError:
        logging.error(f"Could not connect to {url}")
        return False

    except requests.Timeout:
        logging.error(f"Connection to {url} timed out")
        return False


if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.cloudflare.com",
        "https://doesntexist.something.down.test.com",
    ]
    for url in urls:
        status = ping_host(url)
