import os
from flask import Flask, request, url_for, jsonify, redirect
from werkzeug.utils import secure_filename
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)

#set up the uploads folder
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['mp3', 'pdf'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/post/", methods=['POST'])
@cross_origin()
def post():
    print(request.data)
    # name=request.form[request.data]
    # email=request.form['youremail']
    # myDict = {'a': 2, 'b': 3}
    # print(name)
    data = {"name": "name", "title": "album.title"}
    return jsonify(data)

@app.route("/test/", methods=['GET'])
@cross_origin()
def test():
    data = {"id": 7, "title": "OMG TEST COMPLETE"}
    return jsonify(data)


@app.route('/image/<imageid>', methods=['POST'])
@cross_origin()
def upload_file(imageid):
    print('You are looking at ' +imageid)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/test/')
    return

if __name__ == "__main__":
    app.run()
