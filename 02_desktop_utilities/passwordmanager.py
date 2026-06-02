from cryptography.fernet import Fernet #doing the encryption & decryption for us 
import os #opeerating system to check if file/password already exist


# --- SETUP FUNCTIONS ---
def write_key():
    """Creates a key file if it doesn't exist"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the file"""
    return open("key.key", "rb").read()

# --- INITIALIZATION ---
# 1. Generate key if we don't have one
if not os.path.exists("key.key"):
    write_key()

# 2. Load the key
key = load_key()

# 3. Create the encryption tool
fer = Fernet(key)

# --- ACTION FUNCTIONS ---
def view():
    # Check if file exists first to avoid error
    if not os.path.exists('passwords.txt'):
        print("No passwords stored yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # Clean up the line (remove new line character)
            data = line.rstrip()
            if "|" in data:
                # Separate the user name from the encrypted password
                user, passw = data.split("|")
                try:
                    # Decrypt
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted_pass)
                except:
                    print("Error decrypting password for", user)

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    # Encrypt the password
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    
    # Save to file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Added!")

# --- MAIN LOOP ---
while True:
    mode = input("View existing passwords or Add new one (view, add), q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")