from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'

#Configuração de conexão PostgreSQL
engine = create_engine("postgresql://qyaidplwokxgaf:59be526e18d66accd0441832ab9add1fa1c56fdcf4b586ee14a26bb0f30ddaca@ec2-52-22-136-117.compute-1.amazonaws.com:5432/d99ce040bt6uck")
db = scoped_session(sessionmaker(bind=engine))
app.secret_key = '123456789'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"


#Página inicial
@app.route('/')
def index():
    geo = db.execute('select json_build_array(geo_lat::numeric,geo_long::numeric,id,contato,data) from posts_geo').fetchall()
    db.close()
    return render_template('index.html', Geo_pontos=geo)



#Página de informação do grupo
#@app.route('/sobre')
#def sobreNos():
 #   return render_template('sobre.html')

