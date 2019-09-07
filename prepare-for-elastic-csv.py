import csv
import sys
import json

with open(sys.argv[1], mode="r", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=';')
    for i, r in enumerate(csv_reader):
        if i == 0:  # solve header
            print(*r[:11], f"location", sep=";")
            continue

        # convert lat, long
        if r[11] != "NULL":
            r[11] = float(r[11].replace(",", "."))
        if r[12] != "NULL":
            r[12] = float(r[12].replace(",", "."))

        # filter nonsense lat, lon
        if r[11] != "NULL" and not 48 < r[11] < 51:
            continue
        if r[12] != "NULL" and not 12 < r[12] < 19:
            continue
        
        print(*r[:11], f"{r[11]},{r[12]}", sep=";")
