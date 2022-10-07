from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

import time
from datetime import datetime

start = datetime.now()
start_time = time.time()

files = ["BookIt.exe", "docear.exe", "judo.exe", "klen-library.exe", "KML-Editor.exe", "Lectures.prc", "MathStudio.msi", "Nat-installer.exe", "rephrase_beta.jar", "setup-vs64.exe", "TOEFLditor.exe", "tuxpaint.exe"]
signs = ["BookIt.exe.sign", "docear.exe.sign", "judo.exe.sign", "klen-library.exe.sign", "KML-Editor.exe.sign", "Lectures.prc.sign", "MathStudio.msi.sign", "Nat-installer.exe.sign", "rephrase_beta.jar.sign", "setup-vs64.exe.sign", "TOEFLditor.exe.sign", "tuxpaint.exe.sign"]
valid = 0
with open("PublicKey.pem", "rb") as pubkey:
  key = pubkey.read()
  rsa = RSA.importKey(key)
  for i in range(len(files)):
    with open(files[i],  'rb') as f:
      h = SHA256.new(f.read())
      with open(signs[i], "rb") as s:
        try:
           pkcs1_15.new(rsa).verify(h, s.read())
           print("The signature is valid.")
           valid = i
        except (ValueError, TypeError):
           print("The signature is not valid.")
print("\nValid File: " + files[valid])
end = datetime.now()
print("\nStart time: "  + str(start))
print("End time: "  + str(end))
print("Elapsed time: " + str(time.time() - start_time))