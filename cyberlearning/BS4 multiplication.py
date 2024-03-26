import requests 
from bs4 import BeautifulSoup
import re

url = "https://cyber-learning.fr/cyber-challenge/programmation/calcul2/sujet.php?jeton=exemple"

def find_and_multiply_integers(content, num_digits=5):
    
    # Convertir le contenu en chaîne de caractères
    content_str = content.decode('utf-8')

    # Trouver deux entiers de num_digits chiffres
    pattern = r'\b\d{' + str(num_digits) + r'}\b'
    integers = re.findall(pattern, content_str)
    if len(integers) < 2:
        raise ValueError("Moins de deux entiers de {} chiffres trouvés".format(num_digits))
    
    # Imprimer les deux premiers entiers trouvés
    print("Premier entier : ", integers[0])
    print("Deuxième entier : ", integers[1])

    # Multiplier les deux premiers entiers trouvés
    result = int(integers[0]) * int(integers[1])
    return result

for i in range(1):
    r = requests.get(url)
    content = r.content
    # Imprimer la réponse GET
    print("Réponse GET : ", r.text)
    result = find_and_multiply_integers(content)
    print(result)


headers = {
  "exemple": "exemple"
}


while True:
        result = find_and_multiply_integers(r.content)
        r = requests.post(url, data={ 'resultat' : result },  headers=headers)
        print(r.content)
        # Si la réponse est correcte, sortir de la boucle
        if 'correct' in r.content.decode('utf-8'):
            break
