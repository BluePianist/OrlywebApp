from crypt import methods
from flask import Flask, render_template, request
from calcul import calcul_equipes, calcul_joueurs_presents, get_data

app = Flask (__name__)

joueurs = get_data()
equipes = []

@app.route('/', methods = ['GET'])
def home():
    return render_template("tables.html",data=joueurs)


@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    
    if request.method == 'POST':
        form_data = request.form.getlist("estpresent")
        liste_joueurs_presents = 0
        liste_joueurs_presents = calcul_joueurs_presents(form_data, joueurs)[0]
        # print("ENVOI liste joueurs présents =", liste_joueurs_presents)
        calcul = calcul_equipes(liste_joueurs_presents)
        equipes = calcul[0]
        moyennes_equipes = calcul[1]
        
        # print("ENVOI equipes =", equipes)
        return render_template('data.html', data = calcul)

@app.route("/equipes")
def equipes():
    return render_template("affichage_equipes.html", data=equipes)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
