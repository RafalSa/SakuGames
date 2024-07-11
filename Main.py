import tkinter as tk
from tkinter import messagebox
import json
import random

# Wczytanie danych z pliku JSON
def load_characters_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data["characters"]

# Funkcja do walki
def fight(player, enemy):
    # Obliczenie si³y ataku gracza i wroga jako suma statystyk si³y i zrêcznoœci
    player_strength = player["stats"]["si³a"] + player["stats"]["zrêcznoœæ"]
    enemy_strength = enemy["stats"]["si³a"] + enemy["stats"]["zrêcznoœæ"]

    # Symulacja walki - porównanie si³y ataku
    if player_strength > enemy_strength:
        return True  # Gracz wygrywa
    else:
        return False  # Wrogie postacie wygrywaj¹

# Funkcja do obs³ugi przycisku "Fight!"
def fight_button_clicked():
    chosen_character = var_character.get()
    chosen_enemy = var_enemy.get()

    if chosen_character == "" or chosen_enemy == "":
        messagebox.showwarning("Selection", "Wybierz postaæ i wroga przed rozpoczêciem walki.")
        return

    player = characters[chosen_character]
    enemy = enemies[chosen_enemy]

    # Walka
    if fight(player, enemy):
        result = "Gratulacje! Wygra³eœ walkê."
    else:
        result = "Niestety, przegra³eœ walkê. Powodzenia nastêpnym razem!"

    messagebox.showinfo("Fight Result", result)

# Funkcja do inicjalizacji GUI
def initialize_gui():
    global characters, enemies

    characters = load_characters_from_json('characters.json')
    enemies = {k: v for k, v in characters.items() if k != var_character.get()}

    # Utwórz g³ówne okno
    window = tk.Tk()
    window.title("Character Battle")
    window.geometry("500x300")

    # Wybór postaci
    label_character = tk.Label(window, text="Wybierz postaæ:")
    label_character.pack(pady=10)

    character_options = list(characters.keys())
    var_character.set("")  # Zmienna do przechowywania wyboru postaci
    dropdown_character = tk.OptionMenu(window, var_character, *character_options)
    dropdown_character.pack(pady=10)

    # Wybór wroga
    label_enemy = tk.Label(window, text="Wybierz wroga:")
    label_enemy.pack(pady=10)

    enemy_options = list(enemies.keys())
    var_enemy.set("")  # Zmienna do przechowywania wyboru wroga
    dropdown_enemy = tk.OptionMenu(window, var_enemy, *enemy_options)
    dropdown_enemy.pack(pady=10)

    # Przycisk "Fight!"
    btn_fight = tk.Button(window, text="Fight!", command=fight_button_clicked)
    btn_fight.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    var_character = tk.StringVar()
    var_enemy = tk.StringVar()
    initialize_gui()
