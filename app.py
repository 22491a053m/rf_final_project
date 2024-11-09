from flask import Flask ,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def developer():
    return render_template("a.html")


