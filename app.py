from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")