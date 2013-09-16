import os
from flask import Flask, render_template, request, make_response
from PIL import Image
from werkzeug.utils import secure_filename

dirname, filename = os.path.split(os.path.abspath(__file__))
UPLOAD_FOLDER = dirname+'/static/img'
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def main():
    full_screen = False
    filename = None
    if request.method == 'POST':
        overlay_file = request.files['file']
        if overlay_file and allowed_file(overlay_file.filename):
            filename = secure_filename(overlay_file.filename)
            print filename
            overlay_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        full_screen = True
    return render_template('index.html', full_screen = full_screen, filename = filename)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

