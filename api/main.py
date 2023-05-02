from flask import Flask, request
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dkv79122",
  database="usuario"
)

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def hello():
    email = request.form['email']
    password = request.form['password']

    mycursor = db.cursor()

    sql_command = "INSERT INTO usuarios (email, senha, tipo_usuario) VALUES (%s, %s, %s)"
    values = (email, password, 'Aluno')

    mycursor.execute(sql_command, values)
    db.commit()

    print(email)
    print(password)

    return 'Chegou a api'

app.run()
    

