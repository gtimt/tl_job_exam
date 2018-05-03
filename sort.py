import csv

mycsv = csv.reader(open('output.csv'), delimiter=',')
result = sorted(mycsv, key=lambda x:int(x[1]) if x[1].isdigit() else x[1], reverse=True)

f = open("sorted.csv", "w")
writer = csv.writer(f, delimiter=',')
for r in result:
    writer.writerow(r)
