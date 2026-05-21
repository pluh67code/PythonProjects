import tkinter as tk
BG_COLOR = "grey"
TEXT_COLOR = "white"
class LoginMenu(tk.Frame):
    def __init__(self, app):
        super().__init__(app, bg=BG_COLOR)
        self.title_label = tk.Label(self, text="Login To The App", font=("Arial", 60), bg=BG_COLOR, fg=TEXT_COLOR)
        self.title_label.place(relx=0.5, rely=0.2, relheight=0.2, relwidth=0.7, anchor='center')

        self.username_label = tk.Label(self, text="Username:", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.username_label.place(relx=0.375, rely=0.4, relheight=0.1, relwidth=0.4, anchor='center')

        self.username_entry = tk.Entry(self, font=("Arial", 15))
        self.username_entry.place(relx=0.55, rely=0.4, relheight=0.05, relwidth=0.2, anchor='center')

        self.password_label = tk.Label(self, text="Password:", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.password_label.place(relx=0.375, rely=0.5, relheight=0.1, relwidth=0.4, anchor='center')
        
        self.password_entry = tk.Entry(self, font=("Arial", 15))
        self.password_entry.place(relx=0.55, rely=0.5, relheight=0.05, relwidth=0.2, anchor='center')
        
        self.place(relx=0.5, rely=0.5, relheight=1, relwidth=1, anchor='center')

