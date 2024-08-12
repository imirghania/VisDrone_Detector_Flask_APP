from flask import Flask, render_template, request, session, abort, send_file
from visdrone_det_app.forms import ImageForm
from werkzeug.utils import secure_filename
from visdrone_det_app.utils import build_image_path, process_image
import os


app = Flask(__name__)
app.config.from_object('settings.Config')

BASEDIR = os.path.abspath(os.path.dirname(__file__))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            img = form.image.data
            filename = secure_filename(img.filename)
            # print("-------Image File Name: ", filename)
            if filename != "":
                image_path = build_image_path(filename)
                img.save(image_path)
                session["input_image"] = filename
                return input_image(filename=filename)
        else:
            abort(400)
            # return render_template('partials/default_input_image.html')
    
    return render_template('index.html', form=form)


@app.route('/image/<filename>', methods=['GET'])
def input_image(filename):
    return render_template('partials/input_image.html', filename=filename)


@app.route('/image/<filename>', methods=['GET'])
def output_image(filename):
    return render_template('partials/output_image.html', filename=filename)


@app.route('/processing_activated', methods=['GET'])
def processing_button():
    return render_template('partials/processing_button.html')


@app.route('/processing_done', methods=['POST'])
def download_button():
    return render_template('partials/download_button.html')


@app.route('/process_image', methods=['POST'])
def inference():
    input_image_file_name = session["input_image"]
    process_image(input_image_file_name)
    return output_image(input_image_file_name)


@app.route('/download', methods=['GET'])
def download_image():
    image_name = session["input_image"]
    image_path = build_image_path(image_name, "images/predictions")
    return send_file(image_path, 
                    download_name=f"detection_result_{image_name}",
                    mimetype="image/*",
                    as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)