import os

env = os.environ.get("APP_ENV", "dev")
print(f"Mode : {env}")

nom = input("Ton prénom ? ")
reponse = input("Quel est le port par défaut de HTTP ? ")

if reponse.strip() == "80":
    print(f"Bravo {nom} !")
else:
    print(f"Raté {nom}, la réponse était 80.")