from flask import Flask,render_template,url_for

app = Flask(__name__)


posts=[
    {
        'author': 'Varun ',
        'title':'Post 1',
        'content' : 'first post content',
        'date_posted' : 'March 1, 2019'
    },
    {
        'author' : 'Varun Maddipati',
        'title' : 'Post 2',
        'content' : 'second post content',
        'date_posted' : 'March 5, 2019'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__== '__main__':
    app.run(debug=True)