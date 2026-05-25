import tkinter as tk
from constants import *
from home_menu import HomeMenu
from user_repository import save_user, find_user, username_taken, valid_entries

class LoginMenu(tk.Frame):
    def __init__(self, app):
        super().__init__(app, bg=BG_COLOR)
        self.app = app
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
        command=lambda: self._on_login(self.username_entry.get().strip(), self.password_entry.get().strip()))

        self.signup_button = tk.Button(self, text="Sign Up", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR, 
        command=lambda: self._on_signup(self.username_entry.get().strip(), self.password_entry.get().strip()))

        self.login_button.place(relx=0.5, rely=0.65, relheight=0.075, relwidth=0.3, anchor='center')
        self.signup_button.place(relx=0.5, rely=0.75, relheight=0.075, relwidth=0.3, anchor='center')

        self.log_label = tk.Label(self, text="", font=("Arial", 15), bg=BG_COLOR, fg=TEXT_COLOR)
        self.log_label.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.6, relheight=0.1)

    def _on_login(self, username, password):
        user = find_user(username, password)
        if user:
            self.app.change_frame(HomeMenu, user)
        else:
            self.log("Account not found")

    def _on_signup(self, username, password):
        if username_taken(username):
            self.log("Username taken")
            return

        if not valid_entries(username, password):
            self.log("Invalid entries, P.S. password must contain at least 1 number")
            return
        
        save_user(username, password)
        self.log(f"Signed up as {username}, login to enter!")
        
    def log(self, txt):
        self.log_label.config(text=txt)
    
    