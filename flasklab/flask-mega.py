import flask
import psycopg2

db_params = {
    'dbname': 'thompsonj2',
    'user': 'thompsonj2',
    'password': 'card262chip',
    'host': 'stearns.mathcs.carleton.edu'
}

def connect_to_db():
    return psycopg2.connect(**db_params)

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:DodgerBlue">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_math(num1, num2):
    sum = int(num1) + int(num2)
    the_string = "The sum of the two numbers is " + str(sum) + ".";
    return the_string

@app.route('/pop/<abbrev>')
def my_state(abbrev):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT population FROM statepop WHERE code = %s;", [str(abbrev)])
    result = cur.fetchone()
    cur.close()
    conn.close()
    the_string = "The population of " + abbrev + "is" + result[0] + "."


if __name__ == '__main__':
    my_port = "5128"
    app.run(host='0.0.0.0', port = my_port) 
    
