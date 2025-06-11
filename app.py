from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Crear la base de datos si no existe
def init_db():
    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            cedula TEXT,
            telefono TEXT,
            direccion TEXT,
            tipo_area TEXT,
            estado TEXT,
            hora_entrada TEXT,
            hora_salida TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Ruta principal
@app.route('/')
def index():
    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM visitas')
    visitas = cursor.fetchall()
    conn.close()
    return render_template('index.html', visitas=visitas)

# Ruta para agregar visita
@app.route('/agregar', methods=['POST'])
def agregar():
    datos = (
        request.form['nombre'],
        request.form['cedula'],
        request.form['telefono'],
        request.form['direccion'],
        request.form['tipo_area'],
        request.form['estado'],
        request.form['hora_entrada'],
        request.form['hora_salida']
    )
    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO visitas (
            nombre, cedula, telefono, direccion, tipo_area, estado, hora_entrada, hora_salida
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', datos)
    conn.commit()
    conn.close()
    return redirect('/')

# Ruta para eliminar visita
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM visitas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Ejecutar la aplicación
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

