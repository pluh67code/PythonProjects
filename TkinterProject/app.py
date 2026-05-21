import tkinter as tk
from Menus.start_menu import StartMenu
from Menus.home_menu import HomeMenu
from Menus.login_menu import LoginMenu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WorkoutApp")
        self.resizable(False, False)
        self.configure(bg="grey")
        self.window_w = 1000
        self.window_h = 700
        self.current_frame = None
        self._center_window()
        self.load_start_menu()

    def load_login_menu(self):
        self.delete_ui()
        self.current_frame = LoginMenu(self)

    def load_start_menu(self):
        self.delete_ui()
        self.current_frame = StartMenu(self, start_command=self.load_login_menu)

    def load_home_menu(self):
        self.delete_ui()
        self.current_frame = HomeMenu(self)
        
    def delete_ui(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
    
    def _center_window(self):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - self.window_w) // 2
        y = (screen_h - self.window_h) // 2
        self.geometry(f"{self.window_w}x{self.window_h}+{x}+{y}")


