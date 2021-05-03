from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/información')
def acerca():
    return render_template('información')


if __name__ == '__main__':
    app.run()