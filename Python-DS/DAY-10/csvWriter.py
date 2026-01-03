import csv
with open("DAY-10/StudentsData.csv","w") as data:
    csv_writer=csv.writer(data)
    csv_writer.writerow(["s.no","name","dept"])
    csv_writer.writerow([1,"Tharunika","AIDS"])
    csv_writer.writerow([2,"Vignesh","IT"])
    
