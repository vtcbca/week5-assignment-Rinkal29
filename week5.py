#python program create csv file student.csv(sid,sname,city,contact)
import csv
field=['Sid','Sname','City','Contact']
rows=[[1,'Rinkal','Malad',9900012890],
      [2,'Ronak','Vasai',7639207210],
      [3,'Rekha','Malad',8402847011],
      [4,'Chandrakant','Virar',9327496386],
      [5,'Sana','Nallasopara',6063829375]]
filename="c:\\sqlite3\\csv\\student.csv"
#insert record through user input
l=[]
for i in range(5):
    no=int(input("Enter id:"))
    name=input("Enter name:")
    city=input("Enter city:")
    contact=int(input("Enter contact number:"))
    t=(no,name,city,contact)
    l.append(t)
with open(filename,'w',newline='')as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)
    csvwriter.writerows(l)
# Reading dat from csv file.
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for record in csvreader:
        print(record)
print("Total no.of rows:%d"%(csvreader.line_num))
