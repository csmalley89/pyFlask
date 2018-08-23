from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': "Chris Smalley",
        'title': "Blog Post 1",
        'content': 'First Post Content',
        'date_posted': 'August 23, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
  app.run(debug=True)
