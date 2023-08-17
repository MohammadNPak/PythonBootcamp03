import csv

# f = open("data.csv","a")
# f.write("salam")
# f.close()


# with open("data.csv","a") as f:
#     w = csv.writer(f)
#     w.writerow(["mohammd","dorri"])

with open("csv_data/data1.csv","r") as f:
    r = csv.DictReader(f)
    for row in r:
        if row["name"]=="mohammad":
            print(row)


# integral