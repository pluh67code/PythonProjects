import tkinter as tk
from constants import *
from startup_menu import StartupMenu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WorkoutApp")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        self.window_w = 1000
        self.window_h = 700
        self.current_frame = None
        self._center_window()
        
        self.change_frame(StartupMenu)

    def change_frame(self, frame_cls, *args):
        self.delete_ui()
        self.current_frame = frame_cls(self, *args)
        self.current_frame.place(relx=0.5, rely=0.5, relheight=1, relwidth=1, anchor='center')
        
    def delete_ui(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
    
    def _center_window(self):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - self.window_w) // 2
        y = (screen_h - self.window_h) // 2
        self.geometry(f"{self.window_w}x{self.window_h}+{x}+{y}")


