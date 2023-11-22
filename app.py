from flask import Flask # Import microframework de flask
from flask import render_template, request # importa el metodo render para renderizar plantillas html
from flaskext.mysql import MySQL #importa la libreria mysql que nos permite conectarnos a la DB mysql 

#objeto app (mi aplicacion)
app = Flask(__name__) # Creamos una instacia de la clase Flask (nombre del archivo)

mysql = MySQL() # Creamos una instancia de la clase MySql

#MIS CONFIGURACIONES DE BASE DE DATOS
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'movies_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app) #Inicializo la conexion a la DB

@app.route('/') #creo la ruta para la pagina principal
def index():
    sql = "SELECT * FROM `movies_db`.`movies`;"
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data_movies = cursor.fetchall()
    conn.commit()
    
    #necesito renderizar la plantilla index.html
    return render_template('index.html', movies = data_movies)  

@app.route('/create')
def create():
    return render_template('/create.html')

@app.route('/store', methods=['POST'])
def store():
    nombre = request.form['nombre']
    rating = request.form['rating']
    premios = request.form['premios']
    genero = request.form['genero']
    
    sql = "INSERT INTO `movies_db`.`movies` ( created_at, updated_at, title, rating, awards, release_date, length, genre_id) values (sysdate(), null, '" + nombre + "',"+ rating +","+ premios + ", sysdate(), 1, 1);"
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    return 'PELICULA CREADA CON EXISTO: ' + nombre   

@app.route('/delete/<id>')
def delete(id):
    return ''

@app.route('/delete/<id>')
def edit(id):
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000, debug=True)
