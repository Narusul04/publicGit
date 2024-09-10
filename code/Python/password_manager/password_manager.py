#!python 3
# A simple password manager

from cryptography.fernet import Fernet
import sqlite3
import os
import argparse

KEY_FILE = 'secret.key'

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        return key
    
key = load_key()
cipher_suite = Fernet(key)

# Database name
def get_db_conn():
    return sqlite3.connect('allTimerStuff.db')

def setup_db():
    with get_db_conn() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')



def add_password(service, username, password):
    enc_pass = cipher_suite.encrypt(password.encode())
    with get_db_conn() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                  (service, username, enc_pass))


def get_password(service):
    with get_db_conn() as conn:
        c = conn.cursor()
        c.execute("SELECT username, password FROM passwords WHERE service = ?", (service,))
    result = c.fetchone()
    if result:
        username, enc_pass = result
        dec_pass = cipher_suite.decrypt(enc_pass).decode()
        return username, dec_pass
    return None

def delete_pass(service):
    with get_db_conn() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM passwords WHERE service = ?", (service,))
        if c.rowcount > 0:
            print(f"Password for '{service}' deleted succesfully.")
        else:
            print(f"No password found for '{service}'.")


def main():
    parser = argparse.ArgumentParser(description='Password Manager')
    parser.add_argument('action', choices=['add', 'get', 'delete'],
    help='Action to preform: add or get password')
    parser.add_argument('--service', required=True, help='The name of the service/website (e.g., example.com)')
    parser.add_argument('--username', help='The username')
    parser.add_argument('--password', help='The password')
    args = parser.parse_args()

    setup_db()

    if args.action == 'add':
        if not args.username or not args.password:
            print('Username and password are required to add a new entry.')
            return
        add_password(args.service, args.username, args.password)
        print('Password added successfully.')
    elif args.action == 'get':
        result = get_password(args.service)
        if result:
            username, password = result
            print(f'Username: {username}\nPassword: {password}')
        else:
            print('No password found.')
    elif args.action == 'delete':
        delete_pass(args.service)

if __name__ == '__main__':
    main()
    