from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open("encrypted4.txt", "rb") as data:
  plaintext = open("plaintext.txt", "wb")
  iv = data.read(16)
  f = data.read()
  variable = b'\x85\x07}\\(*\xa9\x92,p\xdb\xa6\xbd\x93`5'
  cipher = AES.new(variable, AES.MODE_CBC, iv)
  data = unpad(cipher.decrypt(f), AES.block_size)
  #plaintext.write(cipher.iv)
  plaintext.write(data)
  plaintext.write(b"\n")
  plaintext.close()