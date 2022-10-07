from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key_file = open("example.key", "rb")
key = key_file.read()
key_file.close()

encrypted = open("example.txt.encrypted", "rb")
iv = encrypted.read(16)
f = encrypted.read()
cipher = AES.new(key, AES.MODE_CBC, iv)
data = unpad(cipher.decrypt(f), AES.block_size)
encrypted.close()
decrypted = open("example.txt", "wb")
decrypted.write(data)
decrypted.close()