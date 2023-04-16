import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.fio.cz/zpravodajstvi/stocklist")

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")

headers = [header.text for header in table.find_all("th")]

rows = []
for row in table.find_all("tr"):
    rows.append([cell.text for cell in row.find_all("td")])

rows.pop(0)

from prettytable import PrettyTable

table = PrettyTable(headers)

for row in rows:
    table.add_row(row)

print(table)
input()