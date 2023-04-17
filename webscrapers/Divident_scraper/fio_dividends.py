import requests
from bs4 import BeautifulSoup

# send a GET request to the website
response = requests.get("https://www.fio.cz/zpravodajstvi/dividendy")

# create a beautifulsoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# find the table in the HTML
table = soup.find("table")

# get the table headers
headers = [header.text for header in table.find_all("th")]

# get the table rows
rows = []
for row in table.find_all("tr"):
    rows.append([cell.text for cell in row.find_all("td")])

rows.pop(0)

# print(headers)
# print(rows)

from prettytable import PrettyTable

table2 = PrettyTable(headers)

for row in rows:
    table2.add_row(row)

print(table2)
input()