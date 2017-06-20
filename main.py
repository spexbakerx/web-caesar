from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

        <form method='POST'>
            <label> Rotate by: <input name="rot" value='{rot}' />{rot}
            </label>
            <textarea name="text" value='{text}'></textarea>
            <input type="submit">
       </form>

    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():

    rot = request.form['rot']
    text = request.form['text']

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]


    return rotated


app.run()
