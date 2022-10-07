import math
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad
import time 
from Crypto.Random import get_random_bytes 
from Crypto.Hash import MD5
    

BLOCKSIZE = 2048
h = MD5.new()
count = 0

with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
_hash = h.digest()
fin = open("e2e2.txt", 'rb')
iv = fin.read(16)
data = fin.read()
fin.close() 
cipher = AES.new(_hash, AES.MODE_CBC, iv)  #  cipher
odD = unpad(cipher.decrypt(data), AES.block_size)
fon = open("plaintext.txt", "wb")
fon.write(odD)
fon.write(b"\n")
fon.close()