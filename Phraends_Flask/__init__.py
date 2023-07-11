from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/phraends")
def about():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)