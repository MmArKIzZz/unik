import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
page=1
while page<=5:
    site = urllib.request.urlopen(f"https://msk.spravker.ru/avtoservisy-avtotehcentry/?page={page}").read().decode()
    patern='(?:[\w\W]*?org-widget-header__title-link">)([^<]+)(?:[\w\W]*?header__meta--location">)\s*([А-я,\- .0-9]*)(?:[\w\W]*?="spec__value">)\s*([^<]*)(?:[\w\W]*?="spec__value">)([\w\W][^<]+)'
    match=re.findall(patern,site)
    print(match)
    page+=1

