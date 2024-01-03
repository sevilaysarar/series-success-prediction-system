import requests
from bs4 import BeautifulSoup

url = 'https://tr.wikipedia.org/wiki/T%C3%BCrk_dizileri_listesi'

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

diziler = soup.find_all("tr")

isimler, linkler, bölüm_adet, sezon_adet, durumlar, yayıncılar = [], [], [], [], [], []


for dizi in diziler[21:]:

  dizi_veriler = dizi.find_all("td")
  if (len(dizi_veriler)) != 5:
    continue

  adı = dizi_veriler[0].text
  try:
    link = dizi_veriler[0].find("a")["href"]
    link = "https://tr.wikipedia.org" + link
  except:
    continue
  bölüm_sayısı = dizi_veriler[1].text
  sezon_sayısı = dizi_veriler[2].text
  durumu = dizi_veriler[3].text
  yayıncı = dizi_veriler[4].text

  isimler.append(adı.replace("\n", ""))
  linkler.append(link)
  bölüm_adet.append(bölüm_sayısı.replace("\n", ""))
  sezon_adet.append(sezon_sayısı.replace("\n", ""))
  durumlar.append(durumu.replace("\n", ""))
  yayıncılar.append(yayıncı.replace("\n", ""))

import pandas as pd
dataset = pd.DataFrame()

dataset = pd.concat([dataset,
           pd.DataFrame(isimler, columns = ["isimler"]),
           pd.DataFrame(linkler, columns = ["linkler"]),
           pd.DataFrame(bölüm_adet, columns = ["bölüm_adet"]),
           pd.DataFrame(sezon_adet, columns = ["sezon_adet"]),
           pd.DataFrame(durumlar, columns = ["durumlar"]),
           pd.DataFrame(yayıncılar, columns = ["yayıncılar"]),
           ],
          axis = 1)


dataset.to_excel("wiki_veriler.xlsx", index = False)