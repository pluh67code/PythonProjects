import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WorkoutApp")
        self.resizable(False, False)
        self.configure(bg="grey")
        self.window_w = 1000
        self.window_h = 700
        self.current_widgets = []
        self._center_window()
        self.load_start_menu()

    def load_start_menu(self):
        self.current_widgets = _setup_start_menu_widgets(self)

    def enter_main_app(self):
        self.current_widgets = _setup_main_app_menu(self)

    def delete_ui(self):
        for widget in self.current_widgets:
            widget.destroy()
    
    def _center_window(self):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - self.window_w) // 2
        y = (screen_h - self.window_h) // 2
        self.geometry(f"{self.window_w}x{self.window_h}+{x}+{y}")

def _setup_start_menu_widgets(app):
    app.delete_ui()
    main_title = tk.Label(text="Workout App", font=("Arial", 60), bg="grey", fg='white')
    start_button = tk.Button(text="Start", font=("Arial", 25), bg="grey", fg="white", command=app.enter_main_app)
    exit_button = tk.Button(text="Exit", font=("Arial", 25), bg="grey", fg="white", command=app.destroy)

    main_title.place(relx=0.5, rely=0.2, anchor='center', relheight=0.2, relwidth=0.6)
    start_button.place(relx=0.5, rely=0.5, anchor='center', relheight=0.1, relwidth=0.3)
    exit_button.place(relx=0.5, rely=0.62, anchor='center', relheight=0.1, relwidth=0.3)
    return [main_title, start_button, exit_button]

def _setup_main_app_menu(app):
    app.delete_ui()
    
