# The Dig Radio

*Hello Dan! Or future assistan of Dan. The following is a brief tutorial of how to upload episodes to The Dig's new website.*

-----


### 0. Setup GITHUB

This website is hosted on GitHub Pages. In the "thedigradio" GitHub repository, all episodes and newsletters are stored in the "_posts" folder. Adding a new file to this folder will cause the website to automatically update within ten minutes.

The user uploading posts should have collaborator permissions with this repository. If you do not have access email andysrickert@gmail.com

### 1. Uploading an episode

This website takes posts in the Markdown markup language. Markdown allows for plain text to be formatted with a very minimal amount of coding. Most of the existing pages use very little Markdown tricks, but if you want to experiment there are [tutorials online](https://commonmark.org/help/). The most relevant skill to learn is linking.

Markdown files can be created in any text editor; simply save the file with a ".md" at the end. Here is an example episode post:

```
---
layout: post
title: "SCOTUS, Politics, and the Law w/ Aziz Rana, Amna Akbar, & Marbre Stahly-Butts"
permalink: podcast/scotus-politics-and-the-law-w-aziz-rana-amna-akbar-marbre-stahly-butts/
audiolink: https://media.blubrry.com/thedig/content.blubrry.com/thedig/The_Dig-EP_355-SCOTUS.mp3
categories: 
- Capitalism
- Labor
tags: 
- Aziz Rana
- Amna Akbar
- Marbre Stahly-Butts
---

A timely interview from the archives: legal scholars Aziz Rana and Amna Akbar, and Movement for Black Lives lawyer Marbre Stahly-Butts, on SCOTUS, liberal court veneration, and other big questions on the law and politics facing the left.

Find Eslanda at haymarketbooks.org/books/1769-eslanda

Support The Dig at Patreon.com/TheDig

```

To make an episode post, copy and paste this text and change it to reflect the new episode.

**layout:** leave this field as "post"

**title:** any title can be given so long as there are quotes around it (these won't show on the page)

**permalink:** This denotes the url of the episode that will appear on the website. Realistically, any permalink can be given, but it is nice to be consistent. Begin with "podcast/" for episodes and then copy and paste the end of the generated url from the blubrry url.

**audiolink:** This is a path of the episode's audiofule. To get this url, go to the episode's page on the wordpress site and click download. A window should open with an audio player. Copy the url for this page and paste it into the audio link box.

**categories:** This is for the Topics metadata. Any number of categories can be added to an episode (or none!) provied each one is given an individual line and begins with "- "

**tags:** The same goes for tags, which is traditionally used for guests.



**Transcript posts** will use the exact format, but leave the audiolink field blank, begin the url with transcripts/ instead of podcasts/, and add "Transcripts" to the tag list. It is also essential that the title begins with "Transcript:"


Titling the markdown file is very important. Here is an example title:

```
2022-05-09-scotus-politics-and-the-law-w-aziz-rana-amna-akbar-marbre-stahly-butts.md
```

The first part of the file name features the date of the episode in YYYY-MM-DD format. If this is forgotten in the file name, the episode will not show on the website. The second half is the episode title. This can technically be anything, but it should match the second part of the permalink field inputted earlier.

Antibody should have "Antibody:" in the title, and Antibody in the categories field.

### 2. Uploading a post

Once you have your Markdown file ready, go to https://github.com/arickert/thedigradio/tree/master/_posts while logged in to your GitHub account with collaborator permissions. In the top right, click "Add file" and then "upload files" on the dropdown.

Drag your episode file into the box at the center page and then click the green "commit changes" button at the bottom of the page.

Your episode is now live, and will show on the website within ten minutes!

 If you want to change an existing episode, you can either manually delete it from the previously linked folder, or you can reupload the updated file. If the reuploaded file has the same name as the older file, it will replace it. Good luck! If you have any questions please email andysrickert@gmail.com


