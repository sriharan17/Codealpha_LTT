import os

from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__, template_folder='../template', static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def home():
    translated = ""
    text = ""

    if request.method == 'POST':
        text = request.form['text']
        source = request.form['source']
        target = request.form['target']

        try:
            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)
        except Exception as e:
            translated = "Translation Error: " + str(e)

    return render_template(
        'index.html',
        translated=translated,
        text=text
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))