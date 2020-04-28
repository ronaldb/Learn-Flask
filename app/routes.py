from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Darrell'},
            'body' : 'This is the first post'
        },
        {
            'author': {'username': 'Anonymous'},
            'body' : 'This is an anonymous post'
        }
    ]

    return render_template('index.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


