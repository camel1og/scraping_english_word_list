import requests
import csv
from bs4 import BeautifulSoup
import time

#自作ファイル読み込み
import ssWrite

#ボット判定回避設定
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
header = {
    'User-Agent': USER_AGENT
}
#URL指定
url = 'https://www.eitangokentei.com/chu1-eitango/'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')#取得データの絞り込み
tds = []#取得データを最後に格納する変数

#スプレットシート接続
workbooks = ssWrite.accessSpleadSheet()
worksheet = workbooks.worksheet('中学一年生単語一覧')
i = 2

for trs in table.find_all('tr'):#for文で英単語を取得
    time.sleep(3)#書き込みスピードを3秒に1回にする（API制限でエラーになるため）
    worksheet.update_cell(i,1, trs.find_all("td")[0].text)
    worksheet.update_cell(i,2, trs.find_all("td")[1].text)
    i += 1
