import csv
import xml.etree.ElementTree as ElT
import requests
import matplotlib.pyplot as plt
import datetime

rounding = 2

data_table = [["Дата", "Доллар США", 'Евро', "Японская иена", 'Украинская гривна']]
xml_roots = []

currencies = {"usd": "R01235", "eur": "R01239", "jpi": "R01820", "uah": "R01720"}
for currency in currencies:
    currency_request = requests.get(
        f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2021&date_req2=14/11/2021&VAL_NM_RQ={currencies[currency]}')
    xml_roots.append(ElT.fromstring(currency_request.text))



for i in range(len(xml_roots[0])):
    row = [xml_roots[0][i].attrib['Date']]
    for root in xml_roots:
        value = float(root[i][1].text.replace(',', '.'))
        nominal = int(root[i][0].text)
        result_value = int((value/nominal)*10**rounding)/10**rounding
        row.append(result_value)
    data_table.append(row)

csvFile = open('result.csv', 'w', newline='')
with csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data_table)

# строим графики
dates = [datetime.datetime.strptime(row[0], "%d.%m.%Y").date() for row in data_table[1:]]
usd = [row[1] for row in data_table[1:]]
eur = [row[2] for row in data_table[1:]]
jpi = [row[3] for row in data_table[1:]]
uah = [row[4] for row in data_table[1:]]
fig, ax = plt.subplots()
ax.plot(dates, usd, label='Доллар США')
ax.plot(dates, eur, label='Евро')
ax.plot(dates, jpi, label='Японская иена')
ax.plot(dates, uah, label='Украинская гривна')
ax.set_title('График валют за год')
ax.legend(loc='lower right')
ax.set_ylabel('Сумма RUB')
ax.set_xlim(xmin=dates[0], xmax=dates[-1])
fig.tight_layout()
plt.show()
