import hashlib

def give_hex(passwd, salt):
    
    encrypted_password = hashlib.pbkdf2_hmac(hash_name= 'sha256', password = passwd.encode(), salt = salt.encode(), iterations = len(salt))
    
    return encrypted_password.hex()