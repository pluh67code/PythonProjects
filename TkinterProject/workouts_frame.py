import tkinter as tk
from workout_frame import WorkoutFrame
from workout import Workout
from exercise import Exercise


class WorkoutsFrame(tk.Frame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame)
        self.workout_frames: list[workout_frame] = []
        
        self.place(relx=0.55, rely=0.5, anchor='center', relwidth=0.65, relheight=0.6)