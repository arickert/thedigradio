from urllib.request import urlopen
from bs4 import BeautifulSoup
import markdownify
import re

def get_names(names):
    # split by comma
    name_list = names.split(',')

    # split by 'and'
    for i in range(len(name_list)-1, -1, -1): # We iterate backwards due to removal of elements
        if ' and ' in name_list[i]:
            temp = name_list[i].split(' and ')
            name_list[i] = temp[0]
            name_list.append(temp[1])
        if not name_list[i].strip(): # If the element is empty after removing white spaces, remove it
            name_list.pop(i)

    # strip leading and trailing spaces
    name_list = [name.strip() for name in name_list]

    return name_list

def remove_duplicates(categories, tags):
    # Use list comprehension to create a new list that consists of only 
    # the elements in categories that are not in themes
    categories = [category for category in categories if category not in tags]

    return categories

page=urlopen("https://thedig.blubrry.net/")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
a=soup.find_all(class_="title")
newep=a[0]["href"]

#### if statement
newpage=urlopen(newep)
newhtml = newpage.read().decode("utf-8")

#vars
date=""
permalink=""
title=""
audiolink=""
categories=[]
tags=[]
body=[]

permalink = newep[slice(27,-1)]+"/"

newsoup = BeautifulSoup(newhtml, "html.parser")
title_soup=newsoup.find(class_="entry-title")
title=title_soup.contents[0]

time_soup=newsoup.find_all("time")[0]
time=time_soup["datetime"].split("T")[0]
date="./_posts/"+time+"-"+permalink[slice(8,-1)]+".md"
# iframe

audiolink= newsoup.find('meta', attrs={'itemprop': 'contentUrl'})['content']


cat_soup=newsoup.find(class_="tags-links")
cont=cat_soup.contents
for a in cont:
    st = a.string
    if "Tagged" not in st:
        if "," not in st:
            categories.append(st)

bod_soup=newsoup.find_all("p")
bod_soup.pop(0)
bod_soup.pop(-1)

for p in bod_soup:
    body.append(markdownify.markdownify(str(p)))
    # print(markdownify.markdownify(p.html))
    # paragraph=""
    # # for item in p.descendants:
    # #     print(item)
    # #     if item.string != None:
    # #         paragraph += item.string
    # body.append(paragraph)

final=body[0][slice(0,10)]
if final == "Featuring ":
    b1=body[0][10:-1]
    onindex=b1.find(" on")
    print(onindex)
    b2=b1[slice(0,onindex)]
    print(b2)
    tags = get_names(b2)

episode="---\nlayout: post\ntitle: "
episode+= '"'+title+'"\npermalink: '+permalink+"\naudiolink: "+audiolink+"\ncategories:\n"
for c in categories:
    episode+= "- "+c+"\n"
episode+="tags:\n"
for t in tags:
    episode+= "- "+t+"\n"
episode +="---\n\n"
for p in body:
    episode+=p
categories=remove_duplicates(categories, tags)
with open(date, 'x') as f:
    f.write(episode)



