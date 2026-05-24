import csv
with open('companies.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('footus.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
                if len(row) > 5 and row[5].strip().lower() == 'international=true':
                    print(row)
