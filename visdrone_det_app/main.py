from flask import Flask, render_template, request, url_for
from visdrone_det_app.forms import ImageForm
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config.from_pyfile('settings.py')

BASEDIR = os.path.abspath(os.path.dirname(__file__))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()

    if form.validate_on_submit():
        img = form.image.data
        filename = secure_filename(img.filename)
        if filename != "":
            img.save(os.path.join(
                BASEDIR, "static", "uploaded_images", filename
                ))
            return input_image(filename=filename)

    return render_template('index.html', form=form)


@app.route('/image/<filename>', methods=['GET'])
def input_image(filename):
    return render_template('partials/input_image.html', filename=filename)


@app.route('/processing_activated', methods=['GET'])
def processing_button():
    return render_template('partials/processing_button.html')


if __name__ == "__main__":
    app.run(debug=True)