from Crypto.Cipher import AES
import base64
import os

def generate_key():
    return os.urandom(16)

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_message(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message)
    nonce = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext
