import json

stats = {
    "wojownik": {
        "stats": {
            "si³a": 10,
            "zrêcznoœæ": 5,
            "wytrzyma³oœæ": 8
        }
    },
    "³ucznik": {
        "stats": {
            "si³a": 5,
            "zrêcznoœæ": 10,
            "wytrzyma³oœæ": 6
        }
    },
    "mag": {
        "stats": {
            "si³a": 3,
            "zrêcznoœæ": 7,
            "wytrzyma³oœæ": 9
        }
    }
}

# Zapisz do pliku JSON
with open('stats.json', 'w') as f:
    json.dump(stats, f, indent=4)
