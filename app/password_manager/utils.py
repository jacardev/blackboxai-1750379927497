import os
import json
from cryptography.fernet import Fernet
from django.conf import settings

# Define paths
DATA_DIR = os.path.join(settings.BASE_DIR, 'data')
JSON_FILE = os.path.join(DATA_DIR, 'records.json')
KEY_FILE = os.path.join(DATA_DIR, 'key.key')

def get_or_create_key():
    """Generate or retrieve the encryption key."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    return key

def load_records():
    """Decrypt and load records from JSON file."""
    key = get_or_create_key()
    fernet = Fernet(key)
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'rb') as file:
            encrypted_data = file.read()
        if not encrypted_data:
            return []
        decrypted_data = fernet.decrypt(encrypted_data)
        records = json.loads(decrypted_data.decode())
        return records
    except Exception as e:
        print(f"Error loading records: {e}")
        return []

def save_records(records):
    """Encrypt and save records into JSON file."""
    key = get_or_create_key()
    fernet = Fernet(key)
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        serialized_data = json.dumps(records).encode()
        encrypted_data = fernet.encrypt(serialized_data)
        with open(JSON_FILE, 'wb') as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        print(f"Error saving records: {e}")
        return False
