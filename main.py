import requests
import csv
from bs4 import BeautifulSoup




#ボット判定回避設定
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
header = {
    'User-Agent': USER_AGENT
}
#URL指定
url = 'https://www.eitangokentei.com/chu1-eitango/'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
#取得確認
# print(soup)


table = soup.find('table')
tds = []
for trs in table.find_all('tr'):
    td = {}
    td["英単語"] = trs.find_all("td")[0].text
    td["日本語"] = trs.find_all("td")[1].text
    tds.append(td)


with open("English_Word.csv", "w", newline= "") as f:
    field_name = ["英単語","日本語"]
    writer = csv.DictWriter(f, fieldnames = field_name)
    writer.writeheader()
    writer.writerows(tds)
    
