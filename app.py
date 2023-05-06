from flask import Flask, render_template, request, redirect
import sqlite3
import time, datetime
import platform, flask

app = Flask(__name__)
db_file = 'components.db'
version = "1.0.7"  # define version variable

def create_table():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS components
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  link TEXT,
                  quantity INTEGER,
                  location TEXT,
                  info TEXT,
                  documentation TEXT,
                  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT * FROM components ORDER BY name ASC')
    components = c.fetchall()
    conn.close()
    return render_template('index.html', components=components)

def get_version():
    return version  # Replace with your version number

@app.context_processor
def inject_version():
    return dict(version=get_version())

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_component():
    if request.method == 'POST':
        name = request.form['name']
        link = request.form['link']
        quantity = request.form['quantity']
        location = request.form['location']
        info = request.form['info']
        documentation = request.form['documentation']
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(
            'INSERT INTO components (name, link, quantity, location, info, documentation, last_update) VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)',
            (name, link, quantity, location, info, documentation))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_component(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT * FROM components WHERE id=?', (id,))
    component = c.fetchone()
    conn.close()
    if request.method == 'POST':
        name = request.form['name']
        link = request.form['link']
        quantity = request.form['quantity']
        location = request.form['location']
        info = request.form['info']
        documentation = request.form['documentation']
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(
            'UPDATE components SET name=?, link=?, quantity=?, location=?, info=?, documentation=?, last_update=CURRENT_TIMESTAMP WHERE id=?',
            (name, link, quantity, location, info, documentation, id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        return render_template('update.html', component=component)

@app.route('/delete/<int:id>')
def delete_component(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('DELETE FROM components WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/add_quantity/<int:id>')
def add_quantity(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('UPDATE components SET quantity=quantity+1 WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/remove_quantity/<int:id>')
def remove_quantity(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('UPDATE components SET quantity=quantity-1 WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/notification')
def notification():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    # Select components with less than 10 quantity
    c.execute('SELECT * FROM components WHERE quantity BETWEEN 1 AND 5')
    low_stock_components_1 = c.fetchall()
    # Select components with less than 10 quantity
    c.execute('SELECT * FROM components WHERE quantity BETWEEN 6 AND 9')
    low_stock_components_2 = c.fetchall()
    conn.close()

    return render_template('notification.html', low_stock_components_1=low_stock_components_1, low_stock_components_2=low_stock_components_2)


@app.route('/about')
def about():
    server_info = {
        'python_version': platform.python_version(),
        'flask_version': flask.__version__,
        'server_os': platform.system(),
    }
    return render_template('about.html', server_info=server_info)

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.datetime.now().year}

@app.route('/low-inventory')
def low_inventory():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM inventory WHERE quantity < 10')
    num_low_inventory = cursor.fetchone()[0]
    connection.close()








if __name__ == '__main__':
    create_table()
    app.run(host="0.0.0.0", debug=True)