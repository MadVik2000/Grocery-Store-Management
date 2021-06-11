import hashlib

def give_hex(passwd):
    encrypted_password = hashlib.sha256(passwd.encode())
    
    return encrypted_password.hexdigest()