import requests 
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import base64

url = "https://cyber-learning.fr/cyber-challenge/programmation/barcode/sujet.php?jeton=exemple"

def fetch_image(img_data):
    img_data = img_data.replace('data:image/png;base64,', '')
    img_data = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_data))
    return img

def decode_qrcode(image):
    decoded_objects = decode(image)      
    if len(decoded_objects) == 0:
        print("Aucun QR code dans l'image")
    else:
        return decoded_objects[0].data.decode("utf-8")

headers = {
  "Exemple" : "Exemple"
}



r = requests.get(url)
for i in range(3):  
    
    print(r.text)  # Imprimez la réponse du GET

    soup = BeautifulSoup(r.content, 'html.parser')
img_data = soup.find('img')['src']
img = fetch_image(img_data)
result = decode_qrcode(img)

for i in range (3):
        result = decode_qrcode(img)
        print(result)
        
        r = requests.post(url, data={ 'codeqr' : result },  headers=headers)
        print(r.content)    
        
        # Si la réponse est correcte, sortir de la boucle
        if 'correct' in r.content.decode('utf-8'):
            break
            