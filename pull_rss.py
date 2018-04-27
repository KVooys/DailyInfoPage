import feedparser
import pprint
import html

def pull_xkcd():
    p = feedparser.parse("https://www.xkcd.com/rss.xml")
    xkcd_dict = {}
    for i in p['entries']:
        pprint.pprint(i)
        print(i['title'], i['summary'], i['link'])
        imgurl = "https://imgs.xkcd.com/comics/" + (i['title'].replace(" ", "_").lower() + ".png")
        print(imgurl)
        xkcd_dict[i['title']] = html.unescape(i['summary'])
    return xkcd_dict


def pull_tweakers():
    p = feedparser.parse("http://feeds.feedburner.com/tweakers/mixed")
    tweakers_dict = {}
    for i in p['entries']:
        tweakers_dict[i['link']] = i['title']
        print(i['link'], i['title'])
    return tweakers_dict

#pull_xkcd()
#pull_tweakers()