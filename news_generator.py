import feedparser
import json

rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

feed = feedparser.parse(rss_url)

haberler = []

for haber in feed.entries[:5]:
    haberler.append({
        "baslik": haber.title,
        "link": haber.link
    })

with open("otomatik-haberler.json", "w", encoding="utf-8") as f:
    json.dump(haberler, f, ensure_ascii=False, indent=4)

print("5 haber kaydedildi.")
