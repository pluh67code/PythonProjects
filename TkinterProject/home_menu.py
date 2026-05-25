import tkinter as tk
from constants import *

class HomeMenu(tk.Frame):
    def __init__(self, app, user):
        super().__init__(app)

        self.banner = tk.Label(self, text="Workouts", font=("Arial", 50), bg=BG_COLOR, fg=TEXT_COLOR)
        self.lower_banner = tk.Label(self, text="", bg=BG_COLOR, fg=TEXT_COLOR)
        self.banner.place(relx=0.5, rely=0.075, relheight=0.15, relwidth=1, anchor='center') 
        self.lower_banner.place(relx=0.5, rely=0.925, relheight=0.15, relwidth=1, anchor='center')

        self.workouts_button = tk.Button(self, text="Workouts", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.prs_button = tk.Button(self, text="PRs", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.history_button = tk.Button(self, text="History", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)

        self.workouts_button.place(relx=0.08, rely=0.29, relheight=0.2, relwidth=0.16, anchor='center')
        self.prs_button.place(relx=0.08, rely=0.5, relheight=0.2, relwidth=0.16, anchor='center')
        self.history_button.place(relx=0.08, rely=0.71, relheight=0.2, relwidth=0.16, anchor='center')