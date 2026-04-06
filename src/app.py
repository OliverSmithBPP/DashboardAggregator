from flask import Flask, render_template


app = Flask(__name__)

if __name__ == 'main':
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html')
 