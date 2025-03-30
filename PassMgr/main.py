from constants import ADD, VIEW, Q
from cryptography.fernet import Fernet

'''
# /This method writes the key into key.key file/
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

def return_key():     # will return the enc key
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

master_pwd = input("Whats the master password? ").strip()
key = return_key() + master_pwd.encode() # encode cuz we are dealing with data in bytes
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as file:
        for line in file:
            user, pwd = (line.strip()).split('|')
            print(f'Username : {user} | Password : {fer.decrypt(pwd.encode()).decode()}')

def add():
    user = input("Username : ")
    pwd = input("Password : ")
    with open('passwords.txt', 'a') as file:
        file.write(user + '|' + fer.encrypt(pwd.encode()).decode() + '\n')  # we are encrypting the password, fer.encrypt takes care of the hard stuff

def main():
    while True:
        try:
            mode = input("What mode would you like to proceed with? ").strip()

            if mode == Q:
                break
            elif mode == ADD:
                add()
            elif mode == VIEW:
                view()
            else:
                raise ValueError

        except ValueError:
            print("Please enter a valid mode")


if __name__ == '__main__':
    main()