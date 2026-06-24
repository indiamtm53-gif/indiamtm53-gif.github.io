import feedparser
import json
import re

rss_kaynaklari = [
"https://feeds.bbci.co.uk/news/world/rss.xml",
"https://feeds.bbci.co.uk/news/technology/rss.xml",
"https://feeds.bbci.co.uk/news/business/rss.xml"
]

def kategori_belirle(baslik):
baslik = baslik.lower()

ekonomi = ["economy", "market", "bank", "money", "inflation", "stock", "business"]
teknoloji = ["technology", "tech", "software", "google", "apple", "microsoft", "ai"]

for kelime in ekonomi:
    if kelime in baslik:
        return "ekonomi"

for kelime in teknoloji:
    if kelime in baslik:
        return "teknoloji"

return "gundem"

def slug_olustur(baslik):
baslik = baslik.lower()
baslik = re.sub(r"[^a-z0-9 ]", "", baslik)
baslik = baslik.replace(" ", "-")
return "auto-" + baslik[:50]

tum_haberler = []

for rss in rss_kaynaklari:
feed = feedparser.parse(rss)

for haber in feed.entries[:3]:
    tum_haberler.append(haber)

haberler = []

for haber in tum_haberler[:5]:

baslik = haber.title
link = haber.link
kategori = kategori_belirle(baslik)
dosya = slug_olustur(baslik) + ".html"

haberler.append({
    "baslik": baslik,
    "link": link,
    "kategori": kategori,
    "dosya": dosya
})

with open("otomatik-haberler.json", "w", encoding="utf-8") as f:
json.dump(haberler, f, ensure_ascii=False, indent=4)

for haber in haberler:

html = f"""

<!DOCTYPE html><html lang="tr">
<head>
<meta charset="UTF-8">
<title>{haber['baslik']}</title>
</head>
<body><h1>{haber['baslik']}</h1><p>Kategori: {haber['kategori']}</p><p>
<a href="{haber['link']}">
Kaynak Habere Git
</a>
</p></body>
</html>
"""with open(haber["dosya"], "w", encoding="utf-8") as f:
    f.write(html)

liste_html = """

<!DOCTYPE html><html lang="tr">
<head>
<meta charset="UTF-8">
<title>Otomatik Haberler</title>
</head>
<body><h1>Otomatik Haberler</h1><ul>
"""for haber in haberler:

liste_html += f"""

<li>
<a href="{haber['dosya']}">
{haber['baslik']}
</a>
</li>
"""liste_html += """

</ul></body>
</html>
"""with open("otomatik-gundem.html", "w", encoding="utf-8") as f:
f.write(liste_html)

print("Otomatik haber sistemi başarıyla çalıştı.")
