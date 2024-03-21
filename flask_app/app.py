from flask import Flask, render_template
from main import *

app = Flask(__name__)


@app.route("/")
def index():
    data = collection.find({}, {"_id": 0})
    return render_template("index.html", data=data)


get_content(html.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
