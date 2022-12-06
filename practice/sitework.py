import requests
import bs4
body=[]
info=[]
final=[]
page_number=1
while page_number<=5:
    page=requests.get('https://msk.spravker.ru/avtoservisy-avtotehcentry/?page='+str(page_number))
    r_page=bs4.BeautifulSoup(page.content, 'html.parser')
    widgets=r_page.find_all("div",class_="org-widget__in")
    for widget in widgets:
        body.append(widget)
    for i in range(0,len(body)):
        d=[]
        name= body[i].find('h3')
        com=body[i].find('p')
        adress = body[i].find('span', class_="org-widget-header__meta org-widget-header__meta--location")
        d.append(name.text.strip())
        d.append(adress.text.strip())
        phone = body[i].find_all('dd')
        for phones in phone:
            d.append(phones.text.strip())
        final.append(d)
    page_number+=1
print(final)

