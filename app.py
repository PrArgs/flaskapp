from flask import Flask, make_response, request, Response

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello')
def hello():
    response = make_response("Hello, World\n")
    response.status_code = 200
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/great/<name>')
def great(name):
    return f"Hello, {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 + num2}"

@app.route('/handle_url_params')
def handle_url_params():
    if request.args.get('greating') and request.args.get('name'):
        greating = request.args['greating']
        name = request.args.get('name')
        return f"{greating}, {name}"
    else:
        return "Please provide a greating and a name"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)