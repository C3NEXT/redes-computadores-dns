from flask import Flask, request, render_template_string, send_file
import mysql.connector
from mysql.connector import Error
import hashlib
import os

app = Flask(__name__, static_folder=".")

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234567Ew7$",  # altere
    "database": "portal_aluno"
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

HTML_SUCESSO = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastro realizado</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center;
               align-items: center; min-height: 100vh; margin: 0; background: #f0f2f5; }
        .card { background: white; padding: 40px; border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,.15); text-align: center; width: 320px; }
        h2 { color: #28a745; margin-top: 0; }
        p  { color: #555; }
        a  { display: inline-block; margin-top: 20px; padding: 10px 24px;
             background: #007bff; color: white; border-radius: 5px; text-decoration: none; }
        a:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="card">
        <h2>✓ Cadastro realizado!</h2>
        <p><strong>RA:</strong> {{ ra }}</p>
        <a href="/">Voltar</a>
    </div>
</body>
</html>
"""

HTML_ERRO = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Erro</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center;
               align-items: center; min-height: 100vh; margin: 0; background: #f0f2f5; }
        .card { background: white; padding: 40px; border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,.15); text-align: center; width: 320px; }
        h2 { color: #dc3545; margin-top: 0; }
        p  { color: #555; }
        a  { display: inline-block; margin-top: 20px; padding: 10px 24px;
             background: #6c757d; color: white; border-radius: 5px; text-decoration: none; }
        a:hover { background: #495057; }
    </style>
</head>
<body>
    <div class="card">
        <h2>✗ {{ titulo }}</h2>
        <p>{{ mensagem }}</p>
        <a href="/">Voltar</a>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/photo.jpg")
def background():
    return send_file("photo.jpg")

@app.route("/login", methods=["POST"])
def cadastrar():
    ra    = request.form.get("ra", "").strip()
    senha = request.form.get("senha", "").strip()

    if not ra or not senha:
        return render_template_string(HTML_ERRO,
            titulo="Campos obrigatórios",
            mensagem="Preencha o RA e a senha.")

    try:
        conn   = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos (ra, senha) VALUES (%s, %s)",
            (ra, senha)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return render_template_string(HTML_SUCESSO, ra=ra)

    except mysql.connector.IntegrityError:
        return render_template_string(HTML_ERRO,
            titulo="RA já cadastrado",
            mensagem=f"O RA {ra} já existe no sistema.")

    except Error as e:
        return render_template_string(HTML_ERRO,
            titulo="Erro no banco",
            mensagem=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)