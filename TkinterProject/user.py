class User:
    def __init__(self, username, password, prs=None, workouts=None, history=None):
        self.username = username
        self.password = password
        self.prs = prs if prs is not None else {}
        self.workouts = workouts if workouts is not None else {}
        self.history = history if history is not None else {}
