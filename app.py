from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


app = Flask(__name__)

#Página inicial
@app.route('/')
def index():
    return render_template('index.html')



#Página de informação do grupo
#@app.route('/sobre')
#def sobreNos():
 #   return render_template('sobre.html')

