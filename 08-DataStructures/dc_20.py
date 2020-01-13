import json 
pc = {
    "name": "DELL",
    "model": "Latitude 5490",
    "screenSize": 13,
    "touchScreen": False,
    "SSD": 256
}

with open ("pc.json", "w") as file:
    file.write(json.dumps(pc, indent=1))
