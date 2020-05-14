#### Server-side source code for personal website ####
# Author: Chris Hein
# Built using Flask

from flask import Flask, render_template, flash, request, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

# Home page
@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title = title)

# Projects redirect
@app.route('/projects/')
def projects():
    title = 'Projects'
    return redirect('/currentprojects/')

# Projects page
@app.route('/currentprojects/')
def current_projects():
    title = 'Projects'
    return render_template('currentprojects.html', title = title)

# Projects page
@app.route('/pastprojects/')
def past_projects():
    title = 'Projects'
    return render_template('pastprojects.html', title = title)


# Contact page
@app.route('/contact/')
def contact():
    title = 'Contact'
    return render_template('contact.html', title = title)

@app.route('/login/')
def login():
    title = 'Login'
    return render_template('login.html', title = title) # can build a login later to view website stats

# Error handling:
@app.errorhandler(404) # handle page not found
def page_not_found(e):
    return 'The server threw a 404 error and this page could not be found. Recheck url spelling and try agian.' # could put in custom html page


if __name__ == '__main__':
    app.run(debug=True) # use ssl_context='adhoc' for quick https)

# deleted some comments
