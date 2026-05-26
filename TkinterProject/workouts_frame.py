import tkinter as tk
from workout_frame import WorkoutFrame
from workout import Workout
from exercise import Exercise


class WorkoutsFrame(tk.Frame):
    def __init__(self, app, ):
        super().__init__(app)
        self.workout_frames: list[workout_frame] = []
        