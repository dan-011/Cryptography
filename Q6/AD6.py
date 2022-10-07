from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 
from Crypto.PublicKey import RSA

key_file = open("example.key.encrypted", "rb")
private_key = RSA.import_key(open("private_key.pem").read())

enc_session_key, nonce, tag, ciphertext = \
  [key_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
key = cipher_aes.decrypt_and_verify(ciphertext, tag)
key_file.close()

decrypted_key = open("example.key", "wb")
decrypted_key.write(key)
decrypted_key.close()