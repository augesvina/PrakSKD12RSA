#!/usr/bin/env python
# coding: utf-8

# In[5]:


import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #menghasilkan kunci public dan private

publickey = key.publickey() # pertukaran kunci public

p = open('plaintext.txt', 'r') #membuka plaintext dari bentuk file
pesan = p.read()

msg = bytes(pesan, 'utf-8')
encryptor = PKCS1_OAEP.new(publickey)
encrypted = encryptor.encrypt(msg)
#pesan untuk mengenkripsi ada di baris di atas 'enkripsi pesan ini

print ('encrypted message:', encrypted) #ciphertext

f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #menuliskan ciphertext dalam bentuk file
f.close()

#decrypted code below

f = open ('encryption.txt', 'r')
msg2 = f.read()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(msg2)))

print ('decrypted Nim = ', decrypted.decode('utf-8'))

f = open ('encryption.txt', 'w')
f.write(str(msg2))
f.write(str(decrypted))
f.close()


# In[ ]:




