from flask import render_template
from app import app
import pull_rss

@app.route('/')
@app.route('/index')
def index():
    xkcd = pull_rss.pull_xkcd()
    tweakers = pull_rss.pull_tweakers()
    return render_template("index.html", xkcd=xkcd, tweakers=tweakers)