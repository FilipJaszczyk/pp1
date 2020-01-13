osoba = { 
    "imie": "Marek", 
    "nazwisko": "Banach", 
    "wiek": 25, 
    "hobby": ["programowanie","wycieczki"], 
    "student": True, 
    "telefon":{"stacjonarny":"2233","komorkowy":"7788"} 
    }

print(osoba["imie"])
osoba["student"] = False
print(osoba["student"])

print("=================")

for x in osoba:
    print(f'"{x}": "{osoba[x]}"')
# same output as:
for x,y in osoba.items():
    print(x,y)

print("=================")

# looping trough all key names in dict
for x in osoba:
    print(x)

print("=================")

# looping trough all values in dict
for x in osoba:
    print(osoba[x])

# adding/removing elements to dict
print("=================")
osoba["gender"] = "male"
osoba["hobby"].append("rower")
osoba["telefon"]["służbowy"] = 99999
print(osoba)

