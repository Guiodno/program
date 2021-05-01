from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "peterson"
    return render_template('index.html', name=name)

@app.route('/blog')
def blog():
    return render_template('blog.html')