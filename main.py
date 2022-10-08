from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name


if __name__ == '__main__':
    app.run()