from urllib.request import urlopen
from bs4 import BeautifulSoup
import markdownify
import re


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

audiolink_soup=newsoup.find_all("iframe")[0]["src"].split("EP_")[1].split(".mp3")[0]
audiolink="https://media.blubrry.com/thedig/content.blubrry.com/thedig/The_Dig-EP_"+audiolink_soup+".mp3"


cat_soup=newsoup.find(class_="tags-links")
cont=cat_soup.contents
catflag=False
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
    pflag=False
    onindex=b1.find(" on")
    b2=b1[slice(0,onindex)]
    while pflag==False:
        com=b2.find(",")
        name = b2[0:com]

        if b2.find(",")== -1:     
            pflag=True

            if b2.find(" and ")>3:
                andloc=b2.find(" and ")
                tags.append(b2[:andloc])
                andloc+=5
                tags.append(b2[andloc:])
                break

        com+=2
        b2=b2[com:]
        tags.append(name)

print(tags)
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

with open(date, 'x') as f:
    f.write(episode)
