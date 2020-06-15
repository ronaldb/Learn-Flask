from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Darrell'},
            'body' : 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.'
        },
        {
            'author': {'username': 'Anonymous'},
            'body' : 'Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.'
        },
        {
            'author': {'username': 'Julius Caesar'},
            'body' : 'Et tu, Brute?'
        }
    ]

    return render_template('index.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


