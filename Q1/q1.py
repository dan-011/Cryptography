import hashlib
import time
from datetime import datetime

start_time = datetime.now()

start = time.time()

checksum = "cbfe1fe1024f4ffc3fe14c5f481be29140686bf76d48a79b2303d923fd99ce68"
files = ["BookIt.exe", "docear.exe", "judo.exe", "klen-library.exe", "KML-Editor.exe", "Lectures.prc", "MathStudio.msi", "Nat-installer.exe", "rephrase_beta.jar", "setup-vs64.exe", "TOEFLditor.exe", "tuxpaint.exe"]
correct_files = []
for _file in files:
  with open(_file, "rb") as f:
    _hash = hashlib.sha256()
    for bytes in iter(lambda: f.read(4096), b""):
      _hash.update(bytes)
    if _hash.hexdigest() == checksum:
      correct_files.append(_file)
      
for _file in correct_files:
  print("Legitimate Program File: " + _file)

print("\nStart time: "  + str(start_time))
print("End time: "  + str(datetime.now()))
print("Elapsed time: " + str(time.time() - start))