import requests
import random
from datetime import datetime
import time

API_URL = "http://192.168.56.1:80/RaspberryProject/PartieAPI/api.php"

def generate_random_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidite = round (random.uniform(40.0, 70.0),2)
    date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return{
        'temperature' : temperature,
        'humidite' : humidite,
        'date' : date
    }

def send_data():
    data = generate_random_data()
    try:
            response = requests.post(API_URL, data=data)
            print(f"[{data['date']}] Envoyé : {data} -> Réponse : {response.text}")
    except requests.exceptions.RequestException as e:
         print ("Erreur de l'envoie:", e)
if __name__ == "__main__":
        while True:
            send_data()
            time.sleep(600)