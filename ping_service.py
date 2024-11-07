import requests

def ping_host(url):
    try:
        response = requests.get(url, timeout=1)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

if __name__ == "__main__":
    urls = ["https://www.google.com", "https://www.cloudflare.com"]
    for url in urls:
        status = ping_host(url)
        print (f"{url} is {'up' if status else 'down'}")