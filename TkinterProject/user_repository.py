from user import User
import pickle
file = "user_data.pkl"

def load_users():
    try:
        with open(file, "rb") as f:
            users = pickle.load(f)
    except EOFError: # end of file error for if its empty
        users = []
    return users

def save_user(username, password):
    users = load_users()
    users.append(User(username, password))

    with open(file, "wb") as f:
        pickle.dump(users, f)

def find_user(username, password):
    users = load_users()
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def username_taken(username):
    return username in [user.username for user in load_users()]

def valid_entries(username, password):
    return username and password and any(char.isdigit() for char in password)