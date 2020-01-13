import json
with open("eur.json") as file:
    data = json.load(file)
    print("NBP – 10 ostatnich notowań EURO")
    print('DATA    \t KUPNO  \tSPRZEDAŻ')
    print("==========================================")
    for x in data["rates"]:
        print(f'{x["effectiveDate"]} \t {x["bid"]} \t {x["ask"]}')
