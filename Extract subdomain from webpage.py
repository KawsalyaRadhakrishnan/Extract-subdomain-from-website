import requests

domain = input ("Enter a domain:")
file = open("text.txt")
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomain:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        request.get(url1)
        list = [url1]
        for i in list:
             print(i)

        requests.get(url2)
        list = [url2]
        for i in list:
            print(i)
