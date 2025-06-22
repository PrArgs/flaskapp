from flask import Flask,render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    mylist = [1,2,3,4,5]
    return render_template('index.html', mylist=mylist)


@app.route('/filter')
def filter():
    sometext = "hello world"
    return render_template('filter.html', sometext=sometext)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filter'))

@app.template_filter('reversed_filter')
def reverses_string(s):
    return s[::-1]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)