from flask import Flask, render_template
from main import *

app = Flask(__name__)
web_scraper = WebScraper()


@app.route("/")
def index():
    data = web_scraper.collection.find({}, {"_id": 0})
    return render_template("index.html", data=data)


html = web_scraper.get_html(url)

if __name__ == "__main__":
    web_scraper.get_content(html.text)
    app.run(host="0.0.0.0", debug=True)
