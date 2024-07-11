import json

stats = {
    "wojownik": {
        "stats": {
            "si�a": 10,
            "zr�czno��": 5,
            "wytrzyma�o��": 8
        }
    },
    "�ucznik": {
        "stats": {
            "si�a": 5,
            "zr�czno��": 10,
            "wytrzyma�o��": 6
        }
    },
    "mag": {
        "stats": {
            "si�a": 3,
            "zr�czno��": 7,
            "wytrzyma�o��": 9
        }
    }
}

# Zapisz do pliku JSON
with open('stats.json', 'w') as f:
    json.dump(stats, f, indent=4)
