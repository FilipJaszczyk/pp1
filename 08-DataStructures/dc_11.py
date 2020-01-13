from GBP import GBP
print("  DATA \t          KURS")
print("=======================")
for x in GBP["rates"]:
    print(f"{x['effectiveDate']} \t {x['mid']}")
