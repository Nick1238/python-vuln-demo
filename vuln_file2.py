# vuln_file2.py
import sqlite3
import jwt
import requests
import hashlib

def insecure_sql_injection(query_param):
    # Уязвимость: SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{query_param}'")
    return cursor.fetchall()


def insecure_jwt_decode(token):
    # Уязвимость: неподтверждённая расшифровка JWT
    decoded = jwt.decode(token, options={"verify_signature": False})
    return decoded


def insecure_requests(url):
    # Уязвимость: SSRF
    r = requests.get(url)
    return r.text


def insecure_password_hash(password):
    # Уязвимость: небезопасный хеш
    return hashlib.md5(password.encode()).hexdigest()
