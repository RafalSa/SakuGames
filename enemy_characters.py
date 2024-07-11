import json

# Wczytanie danych z pliku JSON
with open('characters.json', 'r') as f:
    data = json.load(f)

# Funkcja do wyœwietlania informacji o postaci
def print_character_info(character_name):
    if character_name in data["characters"]:
        character = data["characters"][character_name]
        print(f"Nazwa postaci: {character_name}")
        print("Statystyki:")
        for stat, value in character["stats"].items():
            print(f"- {stat}: {value}")
        if "description" in character:
            print(f"Opis: {character['description']}")
        if "strengths" in character:
            print("Mocne strony:")
            for strength in character["strengths"]:
                print(f"- {strength}")
    else:
        print(f"Postaæ '{character_name}' nie istnieje.")

# Wywo³anie funkcji dla postaci "lis" i "goblin"
print_character_info("lis")
print()
print_character_info("goblin")
