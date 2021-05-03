from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/informacion')
def acerca():
    return render_template('informacion.html')


if __name__ == '__main__':
    app.run()