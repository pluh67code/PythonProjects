import tkinter as tk
from user import User
import pickle

BG_COLOR = "grey"
TEXT_COLOR = "white"
file = "Data/user_data.pkl"

class LoginMenu(tk.Frame):
    def __init__(self, app):
        super().__init__(app, bg=BG_COLOR)
        self.file = file
        self.title_label = tk.Label(self, text="Login To The App", font=("Arial", 60), bg=BG_COLOR, fg=TEXT_COLOR)
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.password_label = tk.Label(self, text="Password:", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)

        self.title_label.place(relx=0.5, rely=0.2, relheight=0.2, relwidth=0.7, anchor='center')
        self.username_label.place(relx=0.375, rely=0.4, relheight=0.1, relwidth=0.4, anchor='center')
        self.password_label.place(relx=0.375, rely=0.5, relheight=0.1, relwidth=0.4, anchor='center')

        self.username_entry = tk.Entry(self, font=("Arial", 15))
        self.password_entry = tk.Entry(self, font=("Arial", 15))

        self.username_entry.place(relx=0.55, rely=0.4, relheight=0.05, relwidth=0.2, anchor='center')
        self.password_entry.place(relx=0.55, rely=0.5, relheight=0.05, relwidth=0.2, anchor='center')
        
        self.login_button = tk.Button(self, text="Login", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR, 
        command=lambda: login(self.username_entry.get(), self.password_entry.get(), app))
        self.signup_button = tk.Button(self, text="Sign Up", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR, 
        command=lambda: signup(self.username_entry.get(), self.password_entry.get(), app))

        self.login_button.place(relx=0.5, rely=0.65, relheight=0.075, relwidth=0.3, anchor='center')
        self.signup_button.place(relx=0.5, rely=0.75, relheight=0.075, relwidth=0.3, anchor='center')

        self.place(relx=0.5, rely=0.5, relheight=1, relwidth=1, anchor='center')

def login(username, password, app):
    users = load_users_from_file()
    for user in users:
        if user.username == username and user.password == password:
            print("logged in!")
            break
    

def signup(username, password, app):
    if not valid_entries(username, password): return

    users = load_users_from_file()
    for user in users:
        if user.username == username:
            print("Username taken!")
            return

    print("ok u signed up")
    users.append(User(username, password))
    with open(file, "wb") as f:
        pickle.dump(users, f)
    

def load_users_from_file():
    try:
        with open(file, "rb") as f:
            users = pickle.load(f)
    except (EOFError, FileNotFoundError):
        users = []
    
    return users
def valid_entries(username, password):
    if not username:
        print("Must enter a username")
        return False
    if not password:
        print("Must enter a password")
        return False
    
    # username and password inputs are there:
    if any(char.isdigit() for char in password):
        return True

    print("Password must contain at least 1 number")
    return False
    
