"""Convert .doc files sent through the interface to PDF, adding a cover page and headers."""
__author__ = 'Edouard Klein <edou -at- rdklein.fr>'
#Some code from http://flask.pocoo.org/docs/0.10/patterns/fileuploads/

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import logging
logging.basicConfig(filename='/tmp/debug.log',level=logging.DEBUG)
from subprocess import check_call


UPLOAD_FOLDER = '/tmp/doc2pdf/'
ALLOWED_EXTENSIONS = set(['doc'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    logging.debug('Request on /')
    if request.method == 'POST':
        logging.debug('POST')
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            logging.debug('saving on '+os.path.join(app.config['UPLOAD_FOLDER'], 'file.doc'))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'file.doc'))
            check_call("/var/www/web_doc2pdf/doc2pdf.sh")
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    logging.debug('GET')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/work_dir/<filename>')
def uploaded_file(filename):
    logging.debug('Request on /work_dir/<something>')
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               'final.pdf')

if __name__ == '__main__':
    app.run()
