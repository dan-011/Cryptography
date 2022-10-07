from Crypto.PublicKey import RSA
key = RSA.generate(1024)
f = open("public_key.pem", "wb")
f.write(key.public_key().export_key('PEM'))
f.close()

f = open("private_key.pem", "wb")
f.write(key.export_key('PEM'))
f.close()