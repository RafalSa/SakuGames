import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib
import uuid

# JSON file to store user data
USER_DATA_FILE = 'users.json'
ICON_FILE_START = r"C:\Users\rafal\source\repos\SakuGames\ICO\1455555011_users-10_icon-icons.com_53271.ico"
ICON_FILE_REGISTER = r"C:\Users\rafal\source\repos\SakuGames\ICO\emblemencryptedlocked_93479.ico"
ICON_FILE_LOGIN = r"C:\Users\rafal\source\repos\SakuGames\ICO\locked-black-padlock-security-interface-symbol_icon-icons.com_54500.ico"

def hash_password(password, salt):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(stored_password, provided_password):
    password, salt = stored_password.split(':')
    return password == hashlib.sha256(salt.encode() + provided_password.encode()).hexdigest()

def save_user(username, password):
    salt = uuid.uuid4().hex
    hashed_password = hash_password(password, salt)
    
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
    else:
        users = {}
    
    users[username] = hashed_password

    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)
    print(f"User {username} registered with password hash {hashed_password}")

def register_user():
    username = entry_username_register.get()
    password = entry_password_register.get()
    if not username or not password:
        messagebox.showwarning("Registration", "Please enter a username and password")
        return
    
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
    else:
        users = {}
    
    if username in users:
        messagebox.showwarning("Registration", "Username already exists. Please choose another username.")
        return
    
    save_user(username, password)
    messagebox.showinfo("Registration", "User registered successfully!")
    entry_username_register.delete(0, tk.END)
    entry_password_register.delete(0, tk.END)
    show_login_window()  # Open login window after successful registration

def login_user():
    username = entry_username_login.get()
    password = entry_password_login.get()
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
        
        if username in users and check_password(users[username], password):
            messagebox.showinfo("Login", "Login successful!")
            window_login.withdraw()  # Hide the login window
            window_start.destroy()  # Close the start window
            open_main_window()  # Open the main window
        else:
            messagebox.showwarning("Login", "Invalid username or password")
    else:
        messagebox.showwarning("Login", "No users found. Please register first.")

def show_registration_window():
    window_start.withdraw()
    window_register.deiconify()

def show_login_window():
    window_register.withdraw()
    window_login.deiconify()

def open_main_window():
    # Utwórz nowe g³ówne okno
    main_window = tk.Tk()
    main_window.title("Main Characters")  # Tytu³ okna
    main_window.geometry("500x300")

    # Dodaj elementy GUI do g³ównego okna
    label_welcome = tk.Label(main_window, text="Welcome to the main window!")
    label_welcome.pack(pady=20)

    # Mo¿esz dodaæ wiêcej widgetów do g³ównego okna tutaj

    # Uruchom g³ówn¹ pêtlê okna
    main_window.mainloop()

# Tworzenie okna startowego
window_start = tk.Tk()
window_start.title("Start")
window_start.geometry("800x500")
window_start.iconbitmap(ICON_FILE_START)  # Ustaw ikonê

btn_register = tk.Button(window_start, text="Register", command=show_registration_window)
btn_register.pack(pady=20)

btn_login = tk.Button(window_start, text="Login", command=show_login_window)
btn_login.pack(pady=20)

# Tworzenie okna rejestracji
window_register = tk.Toplevel(window_start)
window_register.title("Register")
window_register.geometry("800x500")
window_register.iconbitmap(ICON_FILE_REGISTER)  # Ustaw ikonê
window_register.withdraw()

label_username_register = tk.Label(window_register, text="Username:")
label_username_register.pack()
entry_username_register = tk.Entry(window_register)
entry_username_register.pack()

label_password_register = tk.Label(window_register, text="Password:")
label_password_register.pack()
entry_password_register = tk.Entry(window_register, show="*")
entry_password_register.pack()

btn_register = tk.Button(window_register, text="Register", command=register_user)
btn_register.pack(pady=20)

btn_back_register = tk.Button(window_register, text="Back", command=lambda: [window_register.withdraw(), window_start.deiconify()])
btn_back_register.pack()

# Tworzenie okna logowania
window_login = tk.Toplevel(window_start)
window_login.title("Login")
window_login.geometry("800x500")
window_login.iconbitmap(ICON_FILE_LOGIN)  # Ustaw ikonê
window_login.withdraw()

label_username_login = tk.Label(window_login, text="Username:")
label_username_login.pack()
entry_username_login = tk.Entry(window_login)
entry_username_login.pack()

label_password_login = tk.Label(window_login, text="Password:")
label_password_login.pack()
entry_password_login = tk.Entry(window_login, show="*")
entry_password_login.pack()

btn_login = tk.Button(window_login, text="Login", command=login_user)
btn_login.pack(pady=20)

btn_back_login = tk.Button(window_login, text="Back", command=lambda: [window_login.withdraw(), window_start.deiconify()])
btn_back_login.pack()

window_start.mainloop()
