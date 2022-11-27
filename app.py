from flask import Flask, render_template, request, url_for, flash, redirect
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/data", methods=["POST"])
def submit():
    print(request.form)
    with open("data.json","w") as fp:
        json.dump(request.form,fp)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
