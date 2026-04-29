import random
import string

chars=string.punctuation + string.ascii_letters + string.digits + " "
chars=list(chars)
key=chars.copy()

print(chars)
print(key)

random.shuffle(key)
print(key)

plain_text=input("Enter the message that you would like encrypted: ")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
    
print(f"Plain text: {plain_text}")
print(f"Cipher text: {cipher_text}")