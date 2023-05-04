import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


#認証設定
credentials = ServiceAccountCredentials.from_json_keyfile_name('word_write.json',scope)

#OAuth2の資格を使用しログイン
gc = gspread.authorize(credentials)

#スプレットシートキー
SPREADSHEET_KEY = "1aB7mCTFRgGNMBDDiAVjQrh-KcE4DGB2ZiBsebJQ7_VA"

worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

import_value = int(worksheet.acell('A1').value)

export_value = import_value+100
worksheet.update_cell(1,2, export_value)