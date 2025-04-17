import requests
import json

def interact_with_ai():
    api_url = "https://menaylex.com/Tools/api.php"
    while True:
        user_message = input("Tú: ")
        if user_message.lower() in ["salir", "exit"]:
            print("Adiós!")
            break
        payload = {"message": user_message}
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print("IA:", data.get("reply", "No hay respuesta."))
            else:
                print("Error:", response.status_code)
        except Exception as e:
            print("Error al comunicarse con la API:", e)

interact_with_ai()