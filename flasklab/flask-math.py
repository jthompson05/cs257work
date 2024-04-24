import flask

app = flask.Flask(__name__)

#
@app.route('/add/<num1>/<num2>')
def my_display(num1, num2):
    sum = int(num1) + int(num2)
    the_string = "The sum of the two numbers is " + the_string + ".";
    return the_string

if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port) 
    
