users = {"charl1": "chuckerby1", "charl2": "chuckerby2"}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Example usage
login()
