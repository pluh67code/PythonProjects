class User:
    def __init__(self, username, password, prs=None, workouts=None, history=None):
        self.username = username
        self.password = password
        self.prs = prs if prs is not None else {}
        self.workouts = workouts if workouts is not None else {}
        self.history = history if history is not None else {}

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "prs": self.prs,
            "workouts": self.workouts,
            "history": self.history
        }
    
    @classmethod
    def from_dict(cls, dct):
        return cls(dct['username'], dct['password'], dct['prs'], dct['workouts'], dct['history'])