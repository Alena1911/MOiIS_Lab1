import pandas as pd
import csv

inputFile = 'sales.json'
outputFile = 'output.csv'

if __name__ == '__main__':
    pdObj = pd.read_json(inputFile)
    table = [['item', 'country', 'year', 'sales']]
    for i, row in pdObj.iterrows():
        item = row['item']
        lpd = pd.DataFrame(eval(f"[{row['sales_by_country']}]"))
        for country, data in lpd.items():
            for year in data[0].items():
                table.append([item, country, year[0], year[1]])

    csvFile = open(outputFile, 'w', newline='')
    with csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(table)
