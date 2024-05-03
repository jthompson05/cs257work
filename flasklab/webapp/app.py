from flask import Flask, render_template
import random
import psycopg2

app = Flask(__name__)

# Lists of names and adjectives
names = ['Alice', 'Alberto', 'Sara', 'Mohammed']
adjectives = ['Wise', 'Brave', 'Kind', 'Adventurous']
years = ['1992', '2005', '1989', '1997']

# Database connection parameters
db_params = {
    'dbname': 'thompsonj2',
    'port': 5432,
    'user': 'thompsonj2',
    'password': 'card262chip',
    'host': 'localhost'
}

def connect_to_db():
    return psycopg2.connect(**db_params)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_sentence')
def generate_sentence():
    name = random.choice(names)
    adjective = random.choice(adjectives)
    year = random.choice(years)
    
    # Fetch a random city from the database
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT city FROM topcities ORDER BY RANDOM() LIMIT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    city = result[0] if result else 'Unknown City'
    sentence = f'{name} the {adjective} was born in {city} in {year}'
    
    return render_template('sentence.html', sentence=sentence)

if __name__ == '__main__':
    my_port = "5128"
    app.run(host='0.0.0.0', port = my_port) 
