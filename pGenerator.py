#Password generator program
from Crypto.Hash import SHA256
from base64 import b64encode
import os

print("Welcome to the password generator program")

#user enters username
print("Enter a username")
userName = input()

#user enters password
print("Enter a password")
pWord = input()

#32 bit salt
salt = b64encode(os.urandom(32)).hex()

#hashes password
h = SHA256.new()
h.update(pWord.encode('utf-8') + salt.encode('utf-8'))
hashedWord = h.hexdigest()
print(hashedWord)

#creates text file to write to
f = open("pwd.txt", "w+")

#writes to text file
f.write(f"[{userName}, {salt}, {hashedWord}]")
