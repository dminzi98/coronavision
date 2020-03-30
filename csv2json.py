import csv
import json
locations_list = []
with open('latestdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        lat = row["latitude"]
        lng = row["longitude"]
        date = row["date"]
        symp = row["symptomatic"].lower()

        if type(symp) == 0 or 'false':
            symp = 0
        if type(symp) == 1 or 'true':
            symp = 1

        date = '-'.join((date[6:],date[3:5],date[:2]))

        loc_dict = {'date': date, 'position': {'lat': float(lat), 'lng': float(lng)}, 'symptomatic': int(symp)}
        locations_list.append(loc_dict)

        line_count += 1
        if (line_count > 100):
            break

    print(f'Processed {line_count} lines.')
    with open('location_data.json', 'w') as f:
        json.dump(locations_list, f)
