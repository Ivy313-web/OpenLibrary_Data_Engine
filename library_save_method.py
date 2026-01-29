from openpyxl import Workbook
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
def excel_method(kw,all_pages_data):
    wb = Workbook()
    ws = wb.active
    wb.remove(ws)
    for i, j in all_pages_data.items():
        ws_new = wb.create_sheet(title=f"page{i}")
        ws_new.append(['Title', 'Writer', 'Want to read', 'Score', 'Link'])
        for a in j:
            ws_new.append([a['title'], a['writer'], a['want_to_read'], a['score'], a['link']])
    wb.save(f'saving_excel/{kw}_book.xlsx')
    print('Saving successful')


def csv_method(kw,all_pages_data):
    for i,j in all_pages_data.items():
        file_name = f'{kw}_book_{i}.csv'
        with open(file_name, 'w', encoding = 'utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Writer', 'Want to read', 'Score', 'Link'])
            for i in j:
                writer.writerow([i['title'],i['writer'],i['want_to_read'],i['score'],i['link']])
        print(f'saving_csv/{file_name} saving successful')



# w




