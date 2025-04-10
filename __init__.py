from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from cryptography.fernet import InvalidToken
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
@app.route("/decrypt/<texte_chiffre>")
def decrypt(texte_chiffre):
    try:
        result = f.decrypt(texte_chiffre.encode())
        return result.decode()
    except:
        return "Erreur : Impossible de déchiffrer."
      @app.route("/encrypt_custom/<user_key>/<valeur>")
def encrypt_custom(user_key, valeur):
    try:
        f_custom = Fernet(user_key.encode())
        token = f_custom.encrypt(valeur.encode())
        return f"Valeur encryptée avec votre clé : {token.decode()}"
    except Exception as e:
        return f"Erreur d'encryptage : {str(e)}"
      @app.route("/decrypt_custom/<user_key>/<texte_chiffre>")
def decrypt_custom(user_key, texte_chiffre):
    try:
        f_custom = Fernet(user_key.encode())
        valeur = f_custom.decrypt(texte_chiffre.encode())
        return f"Valeur déchiffrée avec votre clé : {valeur.decode()}"
    except InvalidToken:
        return "Erreur : Clé incorrecte ou texte invalide."
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"
if __name__ == "__main__":
  app.run(debug=True)
