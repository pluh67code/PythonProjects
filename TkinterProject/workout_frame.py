import tkinter as tk
from constants import *
from workout import Workout

class WorkoutFrame(tk.Frame):
    def __init__(self, name: str, workout: Workout):
        self.name = name
        self.width = 100
        self.height = 100

        self.name_label = tk.Label(self, text=name, font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.name_label.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.1, anchor='center')
        
    # some grid
    # shows up like ts:
    #########
    #  name #
    #       #
    #       #
    #########