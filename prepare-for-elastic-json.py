import csv
import sys
import json

with open(sys.argv[1], mode="r", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=';')
    for row in csv_reader:
        data = {
            "id": row[0],
            "type": row[1],
            "code": int(row[2]),
            "superior_id": int(row[3]) if row[3] != "NULL" else None,
            "event": row[4],
            "category": row[5],
            "place": row[6],
            "datetime": row[7], 
            "car_type": row[8], 
            "street": row[9], 
            "house_no": row[10], 
            "location": {
                "lat":  float(row[11].replace(",", ".")),
                "lon":  float(row[12].replace(",", ".")),
            } if row[11] != "NULL" and row[12] != "NULL" else None
        }
        print(json.dumps(data))
