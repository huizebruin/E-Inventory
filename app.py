from flask import Flask, render_template, request, redirect, flash, send_file
import sqlite3
import time
import datetime
import platform
import flask
import sys
import os
import requests
import datetime
import csv

app = Flask(__name__)
db_file = 'components.db'
version = "1.0.12"  # define version variable
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent client-side JavaScript access to the cookie
app.config['SESSION_TYPE'] = 'null'  # Disable session management

# Set the directory for uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Set the allowed file extensions


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
                  more_info TEXT,
                  price REAL,
                  currency TEXT,
                  image_path TEXT,
                  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')  # Add the "currency" and "image_path" columns
    conn.commit()
    conn.close()

def insert_log_entry(name, action, details):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Check if the log_entries table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='log_entries'")
    table_exists = c.fetchone()

    if not table_exists:
        # Create the log_entries table if it doesn't exist
        c.execute('''CREATE TABLE log_entries
                     (id INTEGER PRIMARY KEY,
                      name TEXT,
                      action TEXT,
                      details TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()

    # Insert the log entry
    c.execute(
        'INSERT INTO log_entries (name, action, details) VALUES (?, ?, ?)',
        (name, action, details)
    )
    conn.commit()
    conn.close()


@app.route('/upload_db', methods=['POST'])
def upload_db():
    db_file = 'components.db'  # Provide the desired name for the database file
    uploaded_file = request.files['db_file']

    if uploaded_file:
        # Validate the file type and ensure it matches the expected database schema
        if uploaded_file.filename.endswith('.db'):
            # Save the uploaded file to the desired location
            uploaded_file.save(os.path.join(app.root_path, db_file))
            flash('Database file uploaded successfully!')
            return redirect('/')
        else:
            flash('Invalid file format. Please upload a valid SQLite database file (.db).')
            return redirect('/upload_db')
    else:
        flash('No file selected for upload. Please try again.')
        return redirect('/upload_db')

@app.route('/check_db_file')
def check_db_file():
    db_file = 'components.db'

    if os.path.exists(db_file):
        # The database file exists, proceed with normal operations
        return redirect('/')
    else:
        # The database file is missing, prompt the user to upload a file
        return render_template('upload_db.html')




@app.route('/')
def index():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row  # Set the row_factory to return rows as dictionaries
    c = conn.cursor()
    c.execute('SELECT * FROM components ORDER BY name ASC')
    components = c.fetchall()
    conn.close()
    return render_template('index.html', components=components)

@app.route('/product/<int:id>')
def product(id):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row  # Set the row_factory to return rows as dictionaries
    c = conn.cursor()
    c.execute('SELECT * FROM components WHERE id=?', (id,))
    component = c.fetchone()
    conn.close()
    return render_template('product.html', component=component)

def format_price(price):
    return "{:.2f}".format(price)

def get_version():
    return version  # Replace with your version number


@app.context_processor
def inject_version():
    return dict(version=get_version())


@app.route('/home')
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
        more_info = request.form['more_info']
        price = request.form['price']  # Get the price value
        currency = request.form['currency']  # Get the currency value
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(
            'INSERT INTO components (name, link, quantity, location, info, documentation, more_info, price, currency, last_update) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)',
            (name, link, quantity, location, info, documentation, more_info, price, currency))  # Include price and currency in the query
        conn.commit()
        conn.close()
# Insert a log entry for the added component
        insert_log_entry(name, 'Add', f'Component "{name}" was added.')

        return redirect('/')
    else:
        return render_template('add.html', format_price=format_price)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_component(id):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
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
        more_info = request.form['more_info']
        price = request.form['price']  # Get the price value
        currency = request.form['currency']  # Get the currency value
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(
            'UPDATE components SET name=?, link=?, quantity=?, location=?, info=?, documentation=?, more_info=?, price=?, currency=?, last_update=CURRENT_TIMESTAMP WHERE id=?',
            (name, link, quantity, location, info, documentation, more_info, price, currency, id))  # Include price and currency in the query
        conn.commit()
        conn.close()
        # Insert a log entry for the updated component
        insert_log_entry(name, 'Update', f'Component "{name}" was updated.')

        return redirect('/')
    else:
        return render_template('update.html', component=component)


@app.route('/delete/<int:id>')
def delete_component(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT name FROM components WHERE id=?', (id,))
    component_name = c.fetchone()[0]
    c.execute('DELETE FROM components WHERE id=?', (id,))
    conn.commit()
    conn.close()

    # Insert a log entry for the deleted component
    insert_log_entry(component_name, 'Delete', f'Component "{component_name}" was deleted.')

    return redirect('/')


@app.route('/add_quantity/<int:id>')
def add_quantity(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT name FROM components WHERE id=?', (id,))
    component_name = c.fetchone()[0]
    c.execute('UPDATE components SET quantity=quantity+1 WHERE id=?', (id,))
    conn.commit()
    conn.close()

    # Insert a log entry for the quantity increase
    insert_log_entry(component_name, 'Quantity Increase', f'Quantity increased for component "{component_name}".')

    return redirect('/')



@app.route('/remove_quantity/<int:id>')
def remove_quantity(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT name FROM components WHERE id=?', (id,))
    component_name = c.fetchone()[0]
    c.execute('UPDATE components SET quantity=quantity-1 WHERE id=?', (id,))
    conn.commit()
    conn.close()

    # Insert a log entry for the quantity decrease
    insert_log_entry(component_name, 'Quantity Decrease', f'Quantity decreased for component "{component_name}".')

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

    return render_template('notification.html', low_stock_components_1=low_stock_components_1,
                           low_stock_components_2=low_stock_components_2)


@app.route('/about')
def about():
    server_info = {
        'python_version': platform.python_version(),
        'flask_version': flask.__version__,
        'server_os': platform.system(),
    }
    repo_name = 'huizebruin/E-Inventory'
    release = get_latest_release(repo_name)
    return render_template('about.html', last_version=release['tag_name'], server_info=server_info)


def get_latest_release(repo_name):
    url = f'https://api.github.com/repos/{repo_name}/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.datetime.now().year}


@app.route('/low-inventory')
def low_inventory():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM components WHERE quantity < 10')
    num_low_inventory = cursor.fetchone()[0]
    connection.close()
    return render_template('low_inventory.html', num_low_inventory=num_low_inventory)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        if 'export_db' in request.form:
            if export_database():
                return redirect('/download_db')
            else:
                flash('An error occurred during database export.', 'error')
        return redirect('/settings')

    database_size = get_database_size()
    return render_template('settings.html', database_size=database_size)


@app.route('/download_db')
def download_db():
    # Path to the exported database file
    filename = 'database_export.csv'

    # Check if the file exists
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        flash('The exported database file is not available for download.', 'error')
        return redirect('/settings')


def export_database():
    conn = None
    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Export the database file
        cursor.execute('SELECT * FROM components')  # Replace 'components' with your table name
        rows = cursor.fetchall()

        # Generate the export file (e.g., CSV)
        filename = 'db_export_e_inventory.csv'  # Change the file name as needed
        with open(filename, 'w') as file:
            # Write the header
            header = [column[0] for column in cursor.description]
            file.write(','.join(header) + '\n')

            # Write the data rows
            for row in rows:
                file.write(','.join(str(value) for value in row) + '\n')

        return True

    except Exception as e:
        flash(f'An error occurred during database export: {str(e)}', 'error')
        return False

    finally:
        # Close the database connection
        if conn:
            conn.close()


@app.route('/export_db')
def export_db():
    export_database()
    return redirect('/settings')


def get_database_size():
    db_path = os.path.abspath(db_file)
    if os.path.exists(db_path):
        size_bytes = os.path.getsize(db_path)
        size_mb = size_bytes / (1024 * 1024)  # Convert to megabytes
        return round(size_mb, 2)
    else:
        return 0

@app.route('/summary')
def database_summary():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM components')
    total_components = c.fetchone()[0]
    c.execute('SELECT SUM(quantity) FROM components')
    total_quantity = c.fetchone()[0]
    conn.close()
    return render_template('summary.html', total_components=total_components, total_quantity=total_quantity)

@app.route('/logbook')
def logbook():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM log_entries ORDER BY timestamp DESC')
    log_entries = c.fetchall()
    conn.close()

    if not log_entries:
        # If there are no log entries, render a template with a message
        return render_template('logbook_empty.html')

    return render_template('logbook.html', log_entries=log_entries)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error_500.html'), 500

if __name__ == '__main__':
    create_table()
    app.run(host="0.0.0.0")