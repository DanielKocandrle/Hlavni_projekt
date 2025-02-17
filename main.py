from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/odkaz", methods=["GET", "POST"])
def link():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        radio = request.form['Radio']
        return render_template("zkouska.html", username=username, password=password, radio=radio)
    return render_template("link.html")

if __name__ == "__main__":
    app.run(debug=True)
