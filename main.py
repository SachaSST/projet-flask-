from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Définition de la route pour la page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Définition de la route pour la page du formulaire
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connexion à la base de données
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Exécution de la requête SQL pour insérer les données dans la table
        c.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))

        # Enregistrement des modifications et fermeture de la connexion
        conn.commit()
        conn.close()

        # Redirection vers la page de confirmation
        return render_template('confirmation.html', name=name)
    else:
        # Affichage du formulaire
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)