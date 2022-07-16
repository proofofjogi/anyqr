from flask import Flask, render_template, url_for, request
from flask_qrcode import QRcode


app = Flask(__name__)
QRcode(app)


@app.route("/", methods=['POST'])
def connect():
    #qrstring = "string"
    if request.form['text'] is not None:
        qrstring = request.form['text']
    return render_template('qr.html', qrstring=qrstring)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4203, debug=True)
