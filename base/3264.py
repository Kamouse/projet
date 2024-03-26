import base64
import itertools

import pickle

import pickle





# Votre message chiffré
decrypted_text = b'gAAAAABlfJghQF_5HEh7rBOfJ3ejbxvw4h6_v_9Sr9GV5eWe6ziltB5pgZCApkSp6c_krkK3XHoN9fbGZ-tRc7xz4Chi7ixWjRuDfEJ-CHAVJfKJxVrbMfEl1akaKuHHOYDnuZhfezkU'

# Essayer chaque clé



print("Texte déchiffré en base 16 : ", decrypted_text.hex())
print("Texte déchiffré en base 32 : ", base64.b32encode(decrypted_text).decode())
print("Texte déchiffré en base 64 : ", base64.b64encode(decrypted_text).decode())

