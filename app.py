import pandas as pd
import os
import uuid
from flask import Flask, jsonify,render_template, request, Response ,send_from_directory

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'neuralnine' and password == 'password':
            return 'Success'
        else:
            return 'Failure'

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    
    elif (
        file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        or file.content_type == 'application/vnd.ms-excel'
    ):
        df = pd.read_excel(file)
        return df.to_html()
    
    return ""

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)

    response = Response(df.to_csv(index=False), 
                        mimetype='text/csv',
                        headers={'Content-Disposition': 'attachment; filename=result.csv'}
                        )
    return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')

@app.route('/handel_post', methods=['POST'])
def handel_post():
    greeting = request.json['greeting']
    name = request.json['name']
    
    print(f"Received greeting: {greeting}, name: {name}")

    # Save the file on the server
    with open('greetings.txt', 'w') as f:
        f.write(f'{greeting} {name}\n')
    
    return jsonify({'message': 'File saved successfully on server'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)