import csv
with open ("DAY-10/StudentsData.csv","r") as data:
    csv_reader=csv.reader(data)
    for row in csv_reader:
        print(row)