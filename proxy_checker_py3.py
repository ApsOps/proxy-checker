import urllib.request , socket
from pathlib import Path

socket.setdefaulttimeout(180)

# BASE_DIR is gives project location
BASE_DIR = Path(__file__).resolve().parent

# PROXY_LIST is our proxy list based on txt
PROXY_LIST = Path.joinpath(BASE_DIR, "assets/proxy-list.txt")

# Proxy checker
def is_bad_proxy(proxy_ip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': proxy_ip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        urllib.request.urlopen('http://www.google.com')  # change the url address here

    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0

# main
if __name__ == "__main__":
    # read the list of proxy IPs in proxy-list.txt
    with open(PROXY_LIST,"r") as proxy_list:
        for item in proxy_list.readlines():
            if is_bad_proxy(item):
                print("Bad Proxy", item)
            else:
                print(item, "is working")
