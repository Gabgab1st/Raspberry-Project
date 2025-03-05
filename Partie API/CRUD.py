import requests

# URL de base de l'API (remplace par ton vrai endpoint)
BASE_URL = "https://example.com/api"

# Clé API si nécessaire (remplace par la tienne)
HEADERS = {
    "Authorization": "Bearer VOTRE_CLE_API",
    "Content-Type": "application/json"
}

#  Envoyer des données (POST)
def send_data():
    data = {
        "temperature": 22.5,
        "humidity": 60,
        "device": "Raspberry Pi 4"
    }
    response = requests.post(f"{BASE_URL}/data", json=data, headers=HEADERS)
    
    if response.status_code == 201:
        print(" Données envoyées avec succès :", response.json())
    else:
        print(f" Erreur {response.status_code} : {response.text}")

# 2 Récupérer des données (GET)
def get_data():
    response = requests.get(f"{BASE_URL}/data", headers=HEADERS)
    
    if response.status_code == 200:
        print(" Données reçues :", response.json())
    else:
        print(f" Erreur {response.status_code} : {response.text}")

# 3 Modifier des données (PUT)
def update_data(item_id):
    data = {
        "temperature": 23.0,
        "humidity": 55
    }
    response = requests.put(f"{BASE_URL}/data/{item_id}", json=data, headers=HEADERS)
    
    if response.status_code == 200:
        print("Données mises à jour :", response.json())
    else:
        print(f" Erreur {response.status_code} : {response.text}")

# 4 Supprimer des données (DELETE)
def delete_data(item_id):
    response = requests.delete(f"{BASE_URL}/data/{item_id}", headers=HEADERS)
    
    if response.status_code == 204:
        print(" Donnée supprimée avec succès")
    else:
        print(f" Erreur {response.status_code} : {response.text}")

send_data()
get_data()
update_data(1)  # Remplace "1" par l'ID de l'élément à modifier
delete_data(1)  # Remplace "1" par l'ID de l'élément à supprimer