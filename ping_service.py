import os 
import subprocess

def ping_host(host):
    response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    return response.returncode == 0

hosts = ['8.8.8.8', '1.1.1.1', '192.0.2.1']

for host in hosts:
    status = ping_host(host)
    print(f"{host} is {'up' if status else 'down'}")