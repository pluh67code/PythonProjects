import tkinter as tk

BG_COLOR = "grey"
TEXT_COLOR = "white"
class StartMenu(tk.Frame):
    def __init__(self, app, start_command):
        super().__init__(app, bg=BG_COLOR)

        self.main_title = tk.Label(self, text="Workout App", font=("Arial", 60), bg=BG_COLOR, fg=TEXT_COLOR)
        self.main_title.place(relx=0.5, rely=0.2, anchor='center', relheight=0.2, relwidth=0.6)

        self.start_button = tk.Button(self, text="Start", font=("Arial", 25), bg=BG_COLOR, fg=TEXT_COLOR, command=start_command)
        self.start_button.place(relx=0.5, rely=0.5, anchor='center', relheight=0.1, relwidth=0.3)

        self.exit_button = tk.Button(self, text="Exit", font=("Arial", 25), bg=BG_COLOR, fg=TEXT_COLOR, command=app.destroy)
        self.exit_button.place(relx=0.5, rely=0.62, anchor='center', relheight=0.1, relwidth=0.3)
      
        self.place(relx=0.5, rely=0.5, relheight=1, relwidth=1, anchor='center')

