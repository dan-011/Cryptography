import subprocess
import time
from datetime import datetime

start = datetime.now()
print("Start time: "  + str(start))
start = time.time()
checksum = "cbfe1fe1024f4ffc3fe14c5f481be29140686bf76d48a79b2303d923fd99ce68"
files = ["BookIt.exe", "docear.exe", "judo.exe", "klen-library.exe", "KML-Editor.exe", "Lectures.prc", "MathStudio.msi", "Nat-installer.exe", "rephrase_beta.jar", "setup-vs64.exe", "TOEFLditor.exe", "tuxpaint.exe"]
legitimate_files = []
for _file in files:
  output = subprocess.check_output(["sha256sum", "-b", _file])
  output = output.decode('utf-8')
  i = output.index("*") - 1
  if checksum == output[:i].strip():
    legitimate_files.append(_file)

for _file in legitimate_files:
  print("Legitimate Program File: " + _file)

print("End time: "  + str(datetime.now()))
print("Elapsed time: " + str(time.time() - start))