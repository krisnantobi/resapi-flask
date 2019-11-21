from cryptography.fernet import Fernet

PASSWORD_KEY = Fernet.generate_key()