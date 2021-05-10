import requests

domain = input ("Enter a domain:")
file = open("subdomain500.txt",'r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        list = [url1]
        for i in list:
             print(i)

        requests.get(url2)
        list = [url2]
        for i in list:
            print(i)
    except requests.ConnectionError:
        pass
