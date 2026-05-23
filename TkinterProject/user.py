
class User:
    def __init__(self, username, password, prs=dict(), workouts=dict(), history=dict()):
        self.username = username
        self.password = password
        self.prs = prs
        self.workouts = workouts
        self.history = history
