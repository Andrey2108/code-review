from flask import Flask, render_template
from main import *

app = Flask(__name__)


@app.route("/")
def index():
    data = collection.find({}, {"_id": 0})
    return render_template("index.html", data=data)


if __name__ == "__app__":
    get_content(html.text)
    app.run(host="0.0.0.0", debug=True)
