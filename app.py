#for more information see below:
#https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)
# $env:FLASK_DEBUG=1
# flask run
# FLASK_DEBUG=1
app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():

	uploaded_file = request.files['new_file_upload']
	print(f'========= new file is {uploaded_file}')
	if uploaded_file.filename != '':
		uploaded_file.save(uploaded_file.filename)

	return redirect(url_for('index'))


