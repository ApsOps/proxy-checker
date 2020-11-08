import sys
import urllib.request, socket
from threading import Thread

socket.setdefaulttimeout(30)

def check_proxy(pip):
    try:        
        proxy_handler = urllib.request.ProxyHandler({'https': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('https://www.myip.com/')  # change the url address here
        print(pip)
    except urllib.error.HTTPError as e:        
        return e
    except Exception as detail:
        return detail
    return 0

#Example run : echo -ne "192.168.1.1:231\n192.168.1.2:231" | python proxy_checkpy3-async.py
proxies = sys.stdin.readlines()
threads = []

for proxy in proxies:
    thread = Thread( target=check_proxy, args=(proxy.strip(), ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()