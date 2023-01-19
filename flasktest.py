from flask import send_file

@app.route("/image/<path:image_path>")
def image(image_path):
    return send_file("C:\path\to\project\folder\cards"+image_path, mimetype='image/png')