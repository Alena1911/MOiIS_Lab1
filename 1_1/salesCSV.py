import pandas as pd
import csv

inputFile = 'sales.json'
outputFile = 'output.csv'

if __name__ == '__main__':
    pdObj = pd.read_json(inputFile)
    table = [['item', 'country', 'year', 'sales']]
    # идём по товарам
    for i, row in pdObj.iterrows():
        item = row['item']
        lpd = pd.DataFrame(eval(f"[{row['sales_by_country']}]"))
        # идём по странам
        for country, data in lpd.items():
            # идём по годам
            for year in data[0].items():
                # заполняем массив для .csv файла
                table.append([item, country, year[0], year[1]])

    csvFile = open(outputFile, 'w', newline='')
    with csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(table)
