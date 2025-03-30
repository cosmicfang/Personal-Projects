from constants import ADD, VIEW, Q
from cryptography.fernet import Fernet


class KeyManager:
    def __init__(self):
        self.key = self._load_key()

    def _load_key(self):
        with open('key.key', 'rb') as file:
            return file.read()

    def get_key(self):
        return self.key

    def write_key(self):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)


class PasswordManager:
    def _init__(self, key_manager):   # Yaha pe Fernet ka use hoga, it's already a class
        self.fernet = Fernet(key_manager.get_key())

    def encrypt_password(self, password):
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt_password(self, password):
        return self.fernet.decrypt(password.encode()).decode()

class Actions:
    def __init(self, password_manager):
        self.password_manager = password_manager
        self.filename = 'passwords.txt'

    def add(self, username, password):
        encrypted_password = self.password_manager.encrypt_password(password)
        with open(self.filename, 'a') as file:
            file.write(f"{username}|{encrypted_password}")

    def view(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, encryptde_password = line.rstrip().split('|')
                    decrypted_password = self.password_manager.decrypt_password(encryptde_password)
                    print(f"User : {username}, Password : {decrypted_password}")
        except FileNotFoundError:
            print("No saved password")


def main():
    key_manager = KeyManager()
    password_manager = PasswordManager(key_manager)
    actions = Actions(password_manager)

    while True:
        mode = input("What is desired mode?").strip().lower()

        if mode == Q:
            break
        elif mode == ADD:
            username = input("Username : ").strip()
            password = input("Password : ").strip()
            actions.add(username, password)
        elif mode == VIEW:
            actions.view()
        else:
            print("Invalid option. Please enter 'add', 'view', or 'q'.")


if __name__ == '__main__':
    main()