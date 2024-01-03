import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

excel_df = pd.read_excel("wiki_veriler.xlsx")

diziler_detaylar_df = pd.DataFrame()

for i in (range(len(excel_df))):
    print(i, excel_df["isimler"][i])

    link = excel_df["linkler"][i]
    url = link
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    info_box = soup.find_all("table", class_ = "infobox")

    try:
        rows = (info_box[0].find_all("tr"))

        dizi_detay_bilgiler = dict()
        for i in range(len(rows[:20])):
            th_veriler = rows[i].find_all("th")
            td_veriler = rows[i].find_all("td")

            if len(th_veriler) == 1 and len(td_veriler) == 1:

                director_parts = td_veriler[0].decode_contents().split('<br/>')
                names = []
                for part in director_parts:
                    temp_soup = BeautifulSoup(part, 'html.parser')

                    if temp_soup.a:
                        names.append(temp_soup.a.text)
                    else:
                        name = temp_soup.text.split("(")[0].strip()
                        names.append(name)

                dizi_detay_bilgiler[th_veriler[0].text] = names

        for key, value in dizi_detay_bilgiler.items():
            dizi_detay_bilgiler[key] = ', '.join(value)

        df = pd.DataFrame([dizi_detay_bilgiler])
        df.index = [excel_df["isimler"][i]]

        diziler_detaylar_df = pd.concat([diziler_detaylar_df, df], axis = 0)
    
    except:
        empty_df = pd.DataFrame()
        empty_df.index = [excel_df["isimler"][i]]

        diziler_detaylar_df = pd.concat([diziler_detaylar_df, empty_df], axis = 0)

diziler_detaylar_df = diziler_detaylar_df.reset_index(drop=True)

veriseti = pd.concat([excel_df, diziler_detaylar_df], axis = 0)

diziler_detaylar_df.to_excel("diziler_detaylar_df.xlsx")
veriseti.to_excel("veriseti.xlsx")