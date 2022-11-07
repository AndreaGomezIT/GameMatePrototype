from flask import Flask 
from flask import render_template, request, redirect, url_for, session                   
from flaskext.mysql import MySQL
from flask import send_from_directory                                 
import os



app = Flask(__name__)                                                              
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost' 
app.config['MYSQL_DATABASE_USER']='root' 
app.config['MYSQL_DATABASE_PASSWORD']='' 
app.config['MYSQL_DATABASE_DB']='gamemate' 
mysql.init_app(app) 
carpeta = os.path.join('uploads')
app.config['CARPETA']= carpeta    



###################### HOME  #################################
@app.route('/')
def home():
    return render_template('pag/index.html')








































if __name__ == '__main__':                                                                      
    app.run(debug=True)
