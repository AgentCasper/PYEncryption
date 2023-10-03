from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("Important.txt","rb") as file:
    original = file.read()


with open("filekey.key","wb") as filekey:
    filekey.write(key)

with open("filekey.key","rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("Important.txt","rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open("Important.txt","wb") as encrypt_file:
    encrypt_file.write(encrypted)

    
    