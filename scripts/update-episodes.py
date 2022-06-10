from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

####edge case italics

page=urlopen("https://thedig.blubrry.net/")
html = page.read().decode("utf-8")
# print(html)
soup = BeautifulSoup(html, "html.parser")
a=soup.find_all(class_="title")
newep=a[0]["href"]

#### if statement
# newep="https://thedig.blubrry.net/podcast/contradictions-with-eric-levitz/"
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

audiolink_soup=newsoup.find_all("iframe")[0]["src"].split("EP_")[1].split(".mp3")[0]
audiolink="https://media.blubrry.com/thedig/content.blubrry.com/thedig/The_Dig-EP_"+audiolink_soup+".mp3"


cat_soup=newsoup.find(class_="tags-links")
cont=cat_soup.contents
catflag=False
for a in cont:
    st = a.string
    if "Tagged" not in st:
        if "," not in st:
            if "Daniel Denvir" in st:
                catflag=True
            else:
                if catflag==False:
                    tags.append(st)
                elif catflag==True:
                    categories.append(st)

bod_soup=newsoup.find_all("p")
bod_soup.pop(0)
bod_soup.pop(-1)

for p in bod_soup:
    paragraph=""
    for item in p.descendants:
        if item.string != None:
            paragraph += item.string
    body.append(paragraph)

episode="---\nlayout: post\ntitle: "
episode+= '"'+title+'"\npermalink: '+permalink+"\naudiolink: "+audiolink+"\ncategories:\n"
for c in categories:
    episode+= "- "+c+"\n"
episode+="tags:\n"
for t in tags:
    episode+= "- "+t+"\n"
episode +="---\n"
for p in body:
    episode+="\n"+p+"\n"
print(episode)
date="./_posts/2022-06-06-the-new-democrats-w-lily-geismer.md"
with open(date, 'x') as f:
    f.write(episode)
