import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import io
import urllib.request
import re
import pytesseract  # Importez la bibliothèque pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR'

url = "https://cyber-learning.fr/cyber-challenge/programmation/captcha/sujet.php?jeton=exemple"

def decode_text(image):
    text = pytesseract.image_to_string(image, lang='fra')  # Utilisez pytesseract pour extraire du texte
    return text

def fetch_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('img')
    img_url = img_tag['src']
    return img_url

def download_image(url):
    response = urllib.request.urlopen(url)
    img_data = response.read()
    img = Image.open(io.BytesIO(img_data))
    return img

headers = {
  "exemple" : "exemple"
}


for i in range(3):  

    r = requests.get(url)
    
    print(r.text)  # Imprimez la réponse du GET

    soup = BeautifulSoup(r.content, 'html.parser')
    img_url = fetch_image(url)
    img = download_image(img_url)
    result = decode_text(img)

    print(result)

    match = result

    print(match)
    
while True:
    r = requests.post(url, data={ 'codeqr' : match },  headers=headers)
    print(r.content)    
        
    # Si la réponse est correcte, sortir de la boucle
    if 'BRAVO' in r.content.decode('utf-8'):
            break


