import requests 
from bs4 import BeautifulSoup
import re

url = "https://www.passetonhack.fr/api/storage/challenges/exemple/transformers/"

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
'''
for i in range(4):
    r = requests.get(url)
    content = r.content
    # Imprimer la réponse GET
    print("Réponse GET : ", r.text)


headers = {
  "Exemple" : "Exemple"
}


    result = find_and_multiply_integers(content)
    print(result)


headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cache-Control": "max-age=0",
  "Content-Length": "21",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "cookieyes-consent=consentid:UVB5VXpSOTFNZnNZeGhRbXNKMXNKb1RNQ2h0clBXODU,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; wordpress_test_cookie=WP%20Cookie%20check; PHPSESSID=f0023ac2b1c49514c39873d0fbe1bb53; FLAG=trop_simple..._Donc_c_est_pas_la_solution.; wfwaf-authcookie-9c9176d3190dfd1358d9c090e85bba0f=316%7Csubscriber%7Cread%7C0c1d7660afe46429f7718e04b73a21cd48333f45510e865f9ad67aafaaf85231; wordpress_logged_in_f2e0ddd3b6b9425a8eec551bcfe163f3=nicolas.coutot%7C1705672565%7C4Hv2XWNUsXtmLCjX0ioiPNlc8EtiqFhnBgnUe90VlRI%7C1ab9da887fe059701ae581a1a8cdcdf6efcfdc2823152d4a38b30765b6bb2c31",
  "Origin": "https://cyber-learning.fr",
  "Referer": "https://cyber-learning.fr/cyber-challenge/programmation/calcul2/sujet.php?jeton=fGDQ0D3z5K9",
  "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Opera GX\";v=\"106\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
}

'''
while True:
        r = requests.post(url, headers=headers)
        print(r.content)
       
